import re
import requests

import re

def extract_douyin_links(text: str):
    """
    从文本中提取抖音分享链接（包括短链 v.douyin.com 和长链 iesdouyin.com）
    
    参数:
        text (str): 包含抖音链接的文本
    
    返回:
        list[str]: 提取出的抖音链接列表
    """
    # 匹配短链和长链两种格式
    pattern = re.compile(
        r'(https?://(?:v\.douyin\.com|www\.iesdouyin\.com|iesdouyin\.com)[^\s]+)'
    )
    links = pattern.findall(text)
    # 去掉末尾可能的标点符号
    links = [link.rstrip('，。,.!?)]"\'') for link in links]
    return links


# 🧪 示例
if __name__ == "__main__":
    # sample_text = """
    # 抖音视频在这里👉 https://v.douyin.com/iN8y2eYj/
    # 还有一个长链：https://www.iesdouyin.com/share/video/7234567890123456789/?region=CN&mid=1234567890
    # """
    sample_text = "3.38 复制打开抖音，看看【烛不遥的作品】⚡大广西是我的家乡⚡ # 烛不遥 # 广西 # d... https://v.douyin.com/48PMYp6_elQ/ M@j.CU uSY:/ 08/08 "
    result = extract_douyin_links(sample_text)
    print("解析结果：")
    for r in result:
        print(r)
