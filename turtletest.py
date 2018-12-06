from turtle import Turtle
t = Turtle()
t.screen.bgcolor("BLACK")
t.color("BLUE")
t.hideturtle()
t.left(45)

def square(len):
    for s in range(4):
        t.fd(len)
        t.left(90)
square(150)

t.screen.mainloop()