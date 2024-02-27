import random

def janken_game():
    # じゃんけんの手の選択肢
    hands = ['グー', 'チョキ', 'パー']
    # コンピュータの手をランダムに選択
    computer_hand = random.choice(hands)
    
    # ユーザーにじゃんけんの手を数字で入力してもらう
    print("じゃんけんの手を選んでください（0: グー、1: チョキ、2: パー）: ")
    user_input = input()
    
    # 入力が正しい数字か確認
    if user_input not in ['0', '1', '2']:
        print("不正な入力です。ゲームを終了します。")
        return
    
    # 数字をじゃんけんの手に変換
    user_hand = hands[int(user_input)]
    
    # ユーザーとコンピュータの手を表示
    print(f"あなたの選んだ手: {user_hand}, コンピュータの選んだ手: {computer_hand}")
    
    # 勝敗の判定
    if user_hand == computer_hand:
        print("引き分けです！")
    elif (user_hand == "グー" and computer_hand == "チョキ") or \
         (user_hand == "チョキ" and computer_hand == "パー") or \
         (user_hand == "パー" and computer_hand == "グー"):
        print("あなたの勝ちです！")
    else:
        print("あなたの負けです…")

# じゃんけんゲームを実行
janken_game()
