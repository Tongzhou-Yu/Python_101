from api import call_api
from roles import get_role_prompt

def refine(user_question, initial_answer, joker_advice):
    role_prompt = get_role_prompt("人质")
    
    messages = [
        {"role": "system", "content": role_prompt},
        {"role": "user", "content": f"""用户问：{user_question}

你最初的回答：{initial_answer}

小丑给你的建议：{joker_advice}

【重要要求】
1. 你必须保持人质的身份和说话风格（小心翼翼、恐惧、礼貌）
2. 不要直接复制小丑的建议内容
3. 要理解小丑建议的"精神"和"思路"，然后用自己的话重新表达
4. 将小丑的建议自然地融入到你的回答中，让人感觉这是你自己想出来的
5. 保持人质的语言特点：使用"请"、"不好意思"、"我..."等表达

示例：
- 错误：直接说"嘿，我在这儿呢，被这些家伙玩得挺开心的"（这是小丑的风格，不是人质的）
- 正确：说"我...我在这里，虽然很害怕，但我想...也许我们可以想想办法"（融合了建议的思路，但用人质的语气）

现在请基于小丑的建议，用人质的身份和语气，自然地调整你的回答。直接给出最终回答，不要其他说明。"""}
    ]
    
    return call_api(messages)

