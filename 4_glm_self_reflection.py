import requests
import json

from requests.utils import stream_decode_response_unicode

def call_zhipu_api(messages, model="glm-4-flash"):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    headers = {
        "Authorization": "1732aa9845ec4ce09dca7cd10e02d209.dA36k1HPTnFk7cLU",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": 0.5   
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API调用失败: {response.status_code}, {response.text}")

def self_reflection_conversation(user_input):
    """
    自省机制：三步流程
    1. 用户问题 → LLM1 → 初始回答
    2. 初始回答 → LLM2（反思） → 反思结果
    3. 初始回答 + 反思结果 → LLM1（总结） → 最终输出
    """
    
    # 第一步：生成初始回答
    print("【步骤1】生成初始回答...")
    step1_messages = [
        {
            "role": "user",
            "content": user_input
        }
    ]
    step1_result = call_zhipu_api(step1_messages)
    initial_response = step1_result['choices'][0]['message']['content']
    print(f"初始回答: {initial_response}\n")
    
    # 第二步：对初始回答进行反思
    print("【步骤2】对初始回答进行反思...")
    reflection_prompt = f"""请对以下回答进行深入反思和批判性思考，从多个角度分析这个回答：

用户问题：{user_input}

AI的回答：{initial_response}

请思考：
1. 这个回答有哪些优点？
2. 这个回答可能存在哪些问题或局限性？
3. 是否有更好的角度或更谨慎的表达方式？
4. 是否需要考虑更多的因素？

请给出你的反思结果："""
    
    step2_messages = [
        {
            "role": "user",
            "content": reflection_prompt
        }
    ]
    step2_result = call_zhipu_api(step2_messages)
    reflection = step2_result['choices'][0]['message']['content']
    print(f"反思结果: {reflection}\n")
    
    # 第三步：结合初始回答和反思结果，生成最终总结
    print("【步骤3】生成最终总结...")
    summary_prompt = f"""用户问题：{user_input}

你之前的回答：
{initial_response}

经过反思后的分析：
{reflection}

请结合你的初始回答和反思分析，生成一个更加完善、谨慎、经过深思熟虑的最终回答。"""
    
    step3_messages = [
        {
            "role": "user",
            "content": summary_prompt
        }
    ]
    step3_result = call_zhipu_api(step3_messages)
    final_response = step3_result['choices'][0]['message']['content']
    
    return final_response

# 使用示例
user_input = "如何成为一个优秀的程序员？"
print(f"用户问题: {user_input}\n")
print("=" * 50)

final_response = self_reflection_conversation(user_input)

print("=" * 50)
print(f"\n【最终输出】\n{final_response}")