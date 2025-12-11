from hostage_think import think
from joker_advise import advise
from hostage_refine import refine

def process(user_question):
    print("\n[步骤1] 人质正在思考...")
    initial_answer = think(user_question)
    print(f"人质初步回答：{initial_answer}\n")
    
    print("[步骤2] 小丑正在给人质建议...")
    joker_advice = advise(user_question, initial_answer)
    print(f"小丑建议：{joker_advice}\n")
    
    print("[步骤3] 人质正在调整回答...")
    final_answer = refine(user_question, initial_answer, joker_advice)
    print(f"人质最终回答：{final_answer}\n")
    
    return {
        "question": user_question,
        "initial_answer": initial_answer,
        "joker_advice": joker_advice,
        "final_answer": final_answer
    }

