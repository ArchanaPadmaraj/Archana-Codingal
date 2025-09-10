import turtle
pen = turtle.Turtle()
pen.speed(1)
pen.color("green")
pen.fillcolor("black")
pen.begin_fill()
for i in range (4):
    pen.forward(100)
    pen.right(90)
pen.end_fill()
turtle.done
