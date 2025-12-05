import requests
from datetime import datetime

try:
    from config import JSONBIN_BIN_ID, JSONBIN_ACCESS_KEY
except ImportError:
    JSONBIN_BIN_ID = "6930e999ae596e708f822224"
    JSONBIN_ACCESS_KEY = "$2a$10$Vx9xdZLj14w8Tmdy7Bhqwu74fcQVBHN5trY4ABjxztuEdNLjuKT6a"

JSONBIN_URL = f"https://api.jsonbin.io/v3/b/{JSONBIN_BIN_ID}"

def save_latest_reply(text):
    data = {
        "text": text,
        "timestamp": datetime.now().isoformat(),
        "read": False
    }
    
    try:
        response = requests.put(
            JSONBIN_URL,
            json=data,
            headers={"X-Access-Key": JSONBIN_ACCESS_KEY}
        )
        return response.status_code == 200
    except:
        return False

def get_latest_reply():
    try:
        response = requests.get(
            JSONBIN_URL + "/latest",
            headers={"X-Access-Key": JSONBIN_ACCESS_KEY}
        )
        if response.status_code == 200:
            data = response.json().get("record", {})
            if not data.get("read", False):
                data["read"] = True
                requests.put(
                    JSONBIN_URL,
                    json=data,
                    headers={"X-Access-Key": JSONBIN_ACCESS_KEY}
                )
                return {"has_new": True, "text": data.get("text")}
        return {"has_new": False, "text": None}
    except:
        return {"has_new": False, "text": None}

