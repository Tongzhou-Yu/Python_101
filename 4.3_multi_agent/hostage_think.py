from api import call_api
from roles import get_role_prompt

def think(user_question):
    role_prompt = get_role_prompt("人质")
    
    messages = [
        {"role": "system", "content": role_prompt},
        {"role": "user", "content": f"用户问：{user_question}\n\n请基于你的人质身份，思考一个初步回答。直接给出回答内容，不要其他说明。"}
    ]
    
    return call_api(messages)

