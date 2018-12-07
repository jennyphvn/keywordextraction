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

def plotTopKFreqWordsDoc(document,k):

    d = cs.parser.documentIndex[document][1]

    new_list = []

    for key,value in d.items():
        new_list.append(value)

    unique_list = []
    for nums in new_list:
        if nums in new_list:
            if nums not in unique_list.append(nums):

                ok_list = sorted(unique_list,reverse = True)[:k]

    shift = 0
    for x in good_list :
        drawBar(10+shift, 20, x, 50, 'red')
        shift += 100

def potBottomKFreqWordsDoc(document,k):

    d = cs.parser.documentIndex[document][1]

    n_list = []

    for key,value in d.items():
        n_list.append(value)

    unique_list = []
    for num in n_list:
        if num not in unique_list:
            unique_list.append(num)

    ok_list = sorted(unique_list,reverse=False)[:k]

    shift = 0
    for x in ok_list:
        drawBar(50 + shift, 100, x, 50, 'yellow')
        shift += 100

def plotFreqWordsSizeDoc():

    shift = 0
    for doc in documents:
        drawBar(90 + shift, 180, cs.stats.plotFreqWordsSizeDoc(document,word), 50, 'blue')
        shift += 100
    update() # Render image
#added code from http://interactivepython.org/runestone/static/CS152f17/Functions/ATurtleBarChart.html in comments because IDK if you will want to use it or not
#I'm trying to help without deleting anything ok
#Ok
