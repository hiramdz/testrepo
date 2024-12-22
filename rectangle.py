'''
Author: Javier Hiram Mendez
Date: 09/10/2021
Class: ISTA 130
Section Leader: Quan Minh Le

Description:
The goal of this program is to draw one rectangle or more using Turtle and by defining and calling functions.
'''

import turtle

# Define a rectangle()
def rectangle(a_turtle, width, height):
    '''
    This function draws a rectangle with a height of
    "height" and a width of "width".
    Parameter:
    :a_turtle: a turtle object
    :width: an int, width of rectangle.
    :height: an int, height of rectangle
    Return:
    None
    '''
    a_turtle.forward(height)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(height)
    a_turtle.right(90)
    a_turtle.forward(width)
    return None

def square(a_turtle, side_len):
    '''
    Makes a square where each of the side lengths of the square
    is the value passed to the parameter 'side_len'
    Parameters:
    :a_turtle: a turtle object
    :side_len: an int, length of a side of the square.
    Returns:
    None
    '''
    a_turtle.forward(side_len)
    a_turtle.right(90)
    a_turtle.forward(side_len)
    a_turtle.right(90)
    a_turtle.forward(side_len)
    a_turtle.right(90)
    a_turtle.forward(side_len)
    return None

def create_space(a_turtle):
    '''
    This function creates a space between shapes.
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.penup()
    a_turtle.forward(25)
    a_turtle.pendown()

def main():
    '''
    This module creates a turtle and draws two rectangles and two squares.
    '''

    # I chose to have my 'turtle' be in the shape of a turtle, a pensize of 10, and will start drawing facing north.
    mywhitecat = turtle.Turtle()
    mywhitecat.shape('turtle')
    mywhitecat.pensize(10)
    mywhitecat.left(90)

    #Draw a red rectangle
    mywhitecat.pencolor('red')
    rectangle(mywhitecat, 150, 300)
    create_space(mywhitecat)
    #Draw a yellow square
    mywhitecat.pencolor('yellow')
    square(mywhitecat, 150)
    create_space(mywhitecat)
    #Draw a green rectangle
    mywhitecat.pencolor('green')
    rectangle(mywhitecat, 150, 300)
    create_space(mywhitecat)
    #Draw a blue square
    mywhitecat.pencolor('blue')
    square(mywhitecat, 150)

    mywhitecat.getscreen().exitonclick() # Keeps the window open

if __name__ == '__main__':
    main()
