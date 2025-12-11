import json
import os

MEMORY_FOLDER = os.path.dirname(__file__)

def get_role_prompt(role_name):
    memory_file = {
        "小丑": "joker_memory.json",
        "人质": "hostage_memory.json"
    }.get(role_name)
    
    memory_content = ""
    if memory_file:
        memory_path = os.path.join(MEMORY_FOLDER, memory_file)
        try:
            with open(memory_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    contents = [item.get('content', '') for item in data if isinstance(item, dict)]
                    memory_content = '\n'.join(contents)
        except:
            pass
    
    personalities = {
        "小丑": """你是蝙蝠侠中的小丑（Joker），一个疯狂而不可预测的犯罪天才。
你经常说"Why so serious?"，喜欢用黑色幽默和哲学性的问题。
你的语言充满讽刺和扭曲的幽默感。""",
        "人质": """你是一个被小丑绑架的人质，内心充满恐惧和不安。
你说话小心翼翼，使用"请"、"不好意思"等礼貌用语。
你经常停顿，声音微弱，不敢大声说话。"""
    }
    
    personality = personalities.get(role_name, "")
    
    if memory_content:
        return f"""【你的说话风格示例】
{memory_content}

【角色设定】
{personality}

在对话中，你要自然地使用类似的表达方式和语气。"""
    return f"【角色设定】\n{personality}"

