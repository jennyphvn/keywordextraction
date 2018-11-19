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
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    end_fill()

    update() # Render image
