import re

import requests


URL_PATTERN = re.compile(r"https?://[^\s<>'\"()]+")
TRAILING_URL_PUNCTUATION = "，。,.!?)]}\"'】》、；："
DOUYIN_HOST_PATTERN = re.compile(
    r"^https?://(?:v\.douyin\.com|www\.iesdouyin\.com|iesdouyin\.com)"
)
DOUYIN_SHORT_URL_PATTERN = re.compile(r"^https?://v\.douyin\.com/")
DOUYIN_SHARE_PREFIX_PATTERN = re.compile(r"^\s*\d+(?:\.\d+)?\s*复制打开抖音，看看")
DOUYIN_SHARE_SUFFIX_PATTERN = re.compile(r"\s+[A-Za-z@._]+\s+[A-Za-z@._]+:/\s*\d{2}/\d{2}\s*$")
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/101.0.0.0 Safari/537.36"
)


def extract_urls(text: str) -> list[str]:
    if not text:
        return []

    # 分享文案里通常会混有标题、口令等内容，这里只提取真正的链接部分。
    return [match.rstrip(TRAILING_URL_PUNCTUATION) for match in URL_PATTERN.findall(text)]


def extract_first_url(text: str) -> str:
    # 兼容原本直接输入 URL 的场景，同时支持粘贴“标题 + URL”的分享文本。
    links = extract_urls(text)
    return links[0] if links else text


def resolve_special_share_url(url: str) -> str:
    # 抖音短链通常需要先跳转到最终页面，后续抓取标题和描述才更稳定。
    if not url or not DOUYIN_SHORT_URL_PATTERN.match(url):
        return url

    try:
        with requests.get(
            url,
            headers={"User-Agent": DEFAULT_USER_AGENT},
            timeout=10,
            allow_redirects=True,
            stream=True,
        ) as response:
            return response.url or url
    except requests.RequestException:
        return url


def extract_share_text_metadata(text: str) -> tuple[str | None, str | None]:
    if not text:
        return None, None

    original_text = text.strip()
    extracted_url = extract_first_url(original_text)
    if extracted_url == original_text:
        return None, None

    cleaned_text = original_text.replace(extracted_url, " ")
    cleaned_text = DOUYIN_SHARE_PREFIX_PATTERN.sub("", cleaned_text)
    cleaned_text = DOUYIN_SHARE_SUFFIX_PATTERN.sub("", cleaned_text)
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip(" ，。,.!?;；：")

    if not cleaned_text:
        return None, None

    # 抖音分享文本里通常已经包含视频文案，抓不到网页元数据时可用作兜底标题和描述。
    return cleaned_text, cleaned_text


def extract_douyin_links(text: str) -> list[str]:
    return [link for link in extract_urls(text) if DOUYIN_HOST_PATTERN.match(link)]
