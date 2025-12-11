from orchestrator import process
from logic import should_exit_by_user

def main():
    print("=" * 50)
    print("小丑游戏")
    print("=" * 50)
    
    while True:
        user_question = input("\n请输入你的问题（输入'退出'结束）：")
        
        if should_exit_by_user(user_question):
            print("再见！")
            break
        
        if not user_question.strip():
            continue
        
        result = process(user_question)
        
        print("\n" + "=" * 50)
        print("最终输出：")
        print(result['final_answer'])
        print("=" * 50)

if __name__ == "__main__":
    main()

