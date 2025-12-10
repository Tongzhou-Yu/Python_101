"""JSONBin API客户端模块"""
import requests
from datetime import datetime


def save_to_jsonbin(text, bin_id, access_key):
    """保存文本到JSONBin"""
    if not bin_id or not access_key:
        return False, "请先配置 Bin ID 和 Access Key"
    
    url = f"https://api.jsonbin.io/v3/b/{bin_id}"
    data = {
        "text": text,
        "timestamp": datetime.now().isoformat(),
        "read": False
    }
    
    try:
        response = requests.put(
            url,
            json=data,
            headers={
                "X-Access-Key": access_key,
                "Content-Type": "application/json"
            },
            timeout=10
        )
        if response.status_code == 200:
            return True, "发送成功！"
        else:
            return False, f"发送失败: {response.status_code} - {response.text}"
    except Exception as e:
        return False, f"发生错误: {str(e)}"

