from turtle import *

# count = 4
#
# while count > 0 :
#     print(forward(300))
#     right(90)
#     count = count -1

# steve = 1
# limit = 300
#
# speed(30)
# pencolor('cyan')
#
# while steve < limit :
#     forward(steve)
#     left(89)
#     steve = steve + 1
print ( bgcolor("orange") ) 

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)

done()


# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md
