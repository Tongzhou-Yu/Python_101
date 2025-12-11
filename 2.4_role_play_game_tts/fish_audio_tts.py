import requests
import os
import platform
import time
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import pygame
    pygame.mixer.init()
    HAS_PYGAME = True
except:
    HAS_PYGAME = False

try:
    from config import FISH_AUDIO_API_KEY
except ImportError:
    FISH_AUDIO_API_KEY = ""

FISH_AUDIO_API_URL = "https://fishspeech.net/api/open/tts"
REFERENCE_ID = "4e637eaf-f478-4002-ac8a-d2b1238ef00c"

def play_audio(file_path):
    """播放音频文件"""
    try:
        if HAS_PYGAME:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            clock = pygame.time.Clock()
            while pygame.mixer.music.get_busy():
                clock.tick(10)
        else:
            abs_path = os.path.abspath(file_path)
            system = platform.system()
            if system == "Windows":
                os.system(f'start "" "{abs_path}"')
            elif system == "Darwin":
                os.system(f'afplay "{abs_path}"')
            else:
                os.system(f'mpg123 "{abs_path}" 2>/dev/null || mplayer "{abs_path}" 2>/dev/null')
    except:
        try:
            abs_path = os.path.abspath(file_path)
            system = platform.system()
            if system == "Windows":
                os.system(f'start "" "{abs_path}"')
        except:
            pass

def text_to_speech(text):
    """Fish Audio TTS函数"""
    if not FISH_AUDIO_API_KEY:
        print("警告：Fish Audio API Key 未配置，请在 config.py 中设置 FISH_AUDIO_API_KEY")
        return
    
    try:
        request_data = {
            "reference_id": REFERENCE_ID,
            "text": text,
            "speed": 1.0,
            "volume": 0,
            "version": "s1",
            "format": "mp3"
        }
        
        headers = {
            "Authorization": f"Bearer {FISH_AUDIO_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(FISH_AUDIO_API_URL, json=request_data, headers=headers, timeout=60)
        
        if response.status_code == 200:
            audio_dir = "tts_audio"
            if not os.path.exists(audio_dir):
                os.makedirs(audio_dir)
            
            timestamp = int(time.time())
            audio_file = os.path.join(audio_dir, f"fish_tts_{timestamp}.mp3")
            
            with open(audio_file, 'wb') as f:
                f.write(response.content)
            
            play_audio(audio_file)
        else:
            print(f"Fish Audio TTS 失败: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Fish Audio TTS 错误: {e}")

