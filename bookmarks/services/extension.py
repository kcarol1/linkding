import re


URL_PATTERN = re.compile(r"https?://[^\s<>'\"()]+")
TRAILING_URL_PUNCTUATION = "，。,.!?)]}\"'】》、；："
DOUYIN_HOST_PATTERN = re.compile(
    r"^https?://(?:v\.douyin\.com|www\.iesdouyin\.com|iesdouyin\.com)"
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


def extract_douyin_links(text: str) -> list[str]:
    return [link for link in extract_urls(text) if DOUYIN_HOST_PATTERN.match(link)]
