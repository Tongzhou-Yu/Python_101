"""精灵动画HTML生成模块"""

def get_sprite_html(is_speaking=False, text=""):
    """生成精灵HTML，根据说话状态显示不同动画"""
    speaking_class = "speaking" if is_speaking else "idle"
    status_text = f"正在说: {text[:20]}..." if (is_speaking and text) else "等待说话..."
    
    return f"""
<style>
@keyframes blink {{
    0%, 90%, 100% {{ transform: scaleY(1); }}
    95% {{ transform: scaleY(0.1); }}
}}

@keyframes speak {{
    0%, 100% {{ 
        height: 30px;
        width: 60px;
        border-radius: 0 0 60px 60px;
    }}
    25% {{ 
        height: 15px;
        width: 50px;
        border-radius: 0 0 50px 50px;
    }}
    50% {{ 
        height: 25px;
        width: 70px;
        border-radius: 0 0 70px 70px;
    }}
    75% {{ 
        height: 20px;
        width: 55px;
        border-radius: 0 0 55px 55px;
    }}
}}

.sprite-container {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 40px;
    min-height: 450px;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border-radius: 20px;
}}

.sprite {{
    width: 200px;
    height: 200px;
    position: relative;
    margin: 0 auto 30px;
}}

.sprite-face {{
    width: 200px;
    height: 200px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 50%;
    position: relative;
    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
    transition: transform 0.3s ease;
}}

.sprite-face:hover {{
    transform: scale(1.05);
}}

.sprite-eye {{
    width: 20px;
    height: 30px;
    background: white;
    border-radius: 50%;
    position: absolute;
    top: 60px;
    animation: blink 3s infinite;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}}

.sprite-eye.left {{
    left: 60px;
}}

.sprite-eye.right {{
    right: 60px;
}}

.sprite-mouth {{
    width: 40px;
    height: 20px;
    border: 4px solid white;
    border-top: none;
    border-radius: 0 0 60px 60px;
    position: absolute;
    bottom: 50px;
    left: 50%;
    transform: translateX(-50%);
    transition: all 0.2s ease;
}}

.sprite-mouth.speaking {{
    animation: speak 0.4s infinite;
}}

.status-text {{
    text-align: center;
    font-size: 18px;
    color: #667eea;
    font-weight: bold;
    margin-top: 20px;
    padding: 10px 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}}
</style>

<div class="sprite-container">
    <div class="sprite">
        <div class="sprite-face">
            <div class="sprite-eye left"></div>
            <div class="sprite-eye right"></div>
            <div class="sprite-mouth {speaking_class}"></div>
        </div>
    </div>
    <div class="status-text">{status_text}</div>
</div>
"""

