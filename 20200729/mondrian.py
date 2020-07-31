from turtle import *

def rect (startx, starty, Rwidth, Rheight , color = "white"):
    penup()
    goto(startx,starty)
    pendown()
    count = 2
    fillcolor (color)
    width(10)

    begin_fill()

    while count > 0 :
        forward (Rwidth)
        left (90)
        forward (Rheight)
        left (90)
        count = count - 1
    end_fill()


rect(-100, 0, 400, 400, "red")
rect(-100, -100, 400, 100, "cyan")
rect(-100, -500, 400, 400)

done()

# import random

# fillcolor ('red')
# pensize (7)
# count = 2
# while count > 0 :
#     forward (400 )
#     right (90)
#     forward (300 )
#     right (90)
#     forward (400 )
#     right (90)
#     forward (500)
#     left (90)
#     count = count - 1
#
# begin_fill ()
# forward (200 )
# right (90)
# forward (300 )
# right (90)
# forward (200 )
# right (90)
# forward (300)
# right (90)
# end_fill()
#





# count = 4
# while count > 0 :
#     forward(200)
#     right (90)
#     forward (10)
#     right(90)
#     count = count - 1
#
# count = 2
# width = 150
# height = 200
#
# pencolor("red")
#
# while count > 0 :
#     forward(10)
#     right(90)
#     forward(200)
#     right(90)
#     count = count - 1
