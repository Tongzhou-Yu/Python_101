from api import call_api
from roles import get_role_prompt

def advise(user_question, hostage_answer):
    role_prompt = get_role_prompt("小丑")
    
    messages = [
        {"role": "system", "content": role_prompt},
        {"role": "user", "content": f"""用户问：{user_question}

人质的初步回答：{hostage_answer}

作为小丑，请给人质一个建议，告诉他如何改进这个回答。直接给出建议内容，不要其他说明。"""}
    ]
    
    return call_api(messages)

