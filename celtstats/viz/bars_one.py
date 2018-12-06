"""viz functions

This module does abc

Todo:
    * Clean code
    * Add return values

"""
from turtle import *

def drawBar(x, y, height, width, color) :

    pencolor(color)
    pensize(0)
    penup()
    setposition(x, y)
    pendown()
    fillcolor(color)
    begin_fill()

    forward(width)
    left(90)
    forward(height)
    #write(str(height))
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    end_fill()

    # xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data (KH: in our version these would be the number of times each word occurred)
    # maxheight = max(xs)
    # numbars = len(xs)
    # border = 10


    update() # Render image
#added code from http://interactivepython.org/runestone/static/CS152f17/Functions/ATurtleBarChart.html in comments because IDK if you will want to use it or not
#I'm trying to help without deleting anything ok
