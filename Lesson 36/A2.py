# dont forget parenthesis!
import turtle
pen = turtle.Turtle()
pen.speed(2)
pen.color("cyan")
pen.fillcolor("black")
number_of_sides = 6
side_length = 80
for i in range(number_of_sides):
    pen.forward(side_length)
    pen.right(360/number_of_sides)
turtle.done()