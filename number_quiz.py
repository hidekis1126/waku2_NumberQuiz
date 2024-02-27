import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("数当てゲームへようこそ！1から100までの数を当ててみてね。")

    while True:
        user_guess = input("あなたの予想する数を入力してね: ")
        if not user_guess.isdigit():
            print("数値を入力してください！")
            continue
        else:
            user_guess = int(user_guess)
            
        attempts += 1
        if user_guess < number_to_guess:
            print("もっと大きい数やで")
        elif user_guess > number_to_guess:
            print("もっと小さい数やで")
        else:
            print(f"正解！{attempts}回で当たったね〜！")
            break

guess_number_game()