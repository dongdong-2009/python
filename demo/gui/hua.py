import turtle#从标准库里面引入turtle

def draw_art():
    window=turtle.Screen()#获得一个窗口句柄
    window.bgcolor("blue")#把背景设为蓝色
    brad = turtle.Turtle()
    brad.shape("turtle")  # 形状是一个海龟除了画海龟还可以画箭头，圆圈等等
    brad.color("orange")  # 颜色是橙色
    brad.speed('slow')  # 画的速度是快速
    brad.forward(100)  # 向前走100步
    brad.right(45)  # 然后海龟头向右转45度
    brad.forward(100)  # 继续向前走100步
    brad.right(135)  # 然后有向右转135度
    window.exitonclick()#当点击一下窗口会自动关闭

draw_art()#调用函数