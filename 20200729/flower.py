from turtle import *
import random
fillcolor(random)

for n in range(60):
    penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()



    circle_size = random.randint(10, 40)
    pensize(random.randint(3, 6))

    for i in range(6):
        begin_fill()
        forward (200 )
        right (90)
        forward (30 )
        right (90)
        end_fill()
