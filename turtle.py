# 必要なライブラリをインストール
# !pip install ColabTurtle

# Turtleライブラリをインポート
import ColabTurtle.Turtle as turtle

# 描画エリアの初期化
turtle.initializeTurtle(initial_speed=10) # 描画速度を設定
turtle.bgcolor("white") # 背景色を白に設定
turtle.color("blue") # ペンの色を青に設定

def draw_star(size, color):
    angle = 144
    turtle.color(color)
    turtle.begin_fill()
    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
    turtle.end_fill()

# 星を描画する関数を呼び出し、異なる位置と色で星を描く
turtle.penup()
turtle.goto(100, 200)
turtle.pendown()
draw_star(50, "blue")

turtle.penup()
turtle.goto(200, 50)
turtle.pendown()
draw_star(70, "green")

turtle.penup()
turtle.goto(300, 200)
turtle.pendown()
draw_star(90, "red")

