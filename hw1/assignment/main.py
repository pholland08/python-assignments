"""
Phillip Holland
COSC 5340
Summer 2018
Assignment 1
"""

import turtle


def main():
    sven_main()
    ole_main()
    drawRectangle(turtle.Turtle(), 5, 10)
    multiples_of_5()
    bonus_turtle(15)


def sven_main():

    # Create a turtle called sven.
    sven = turtle.Turtle()

    # Now tell sven to go forward 10.
    sven.forward(10)

    # What is sven's position now?
    print(sven.position())


def ole_main():
    # Create a turtle called Ole.
    ole = turtle.Turtle()

    # Tell Ole to turn right 45 degrees and go forward 50.
    ole.right(45)
    ole.forward(50)
    print(ole.position(), ole.heading())


def drawRectangle(myTurtle: turtle, width: int, height: int):
    """
    Create a new function called drawRectangle that takes three parameters: myTurtle,
                                                                            width,
                                                                            and height.
    """

    myTurtle.forward(width)
    myTurtle.left(90)
    myTurtle.forward(height)
    myTurtle.left(90)
    myTurtle.forward(width)
    myTurtle.left(90)
    myTurtle.forward(height)


def multiples_of_5():
    # Use the range function to create a sequence of the multiples of 5 up to 50
    return range(5, 50, 5)


def bonus_turtle(max_x: int):
    # Bonus question: Use the turtle to plot the function y = x^2.

    max_y = max_x*max_x

    quad1_turtle = turtle.Turtle()
    quad2_turtle = turtle.Turtle()

    draw_axes(max_y, max_y)

    quad1_turtle.setheading(90)
    quad2_turtle.setheading(90)

    # Draw parabola
    for x in range(max_x):
        y = x*x

        quad1_turtle.goto(x, y)
        quad2_turtle.goto(-x, y)


def draw_axes(x_distance: int, y_distance: int):
    draw_y_axis(y_distance)
    draw_x_axis(x_distance)


def draw_y_axis(distance: int):
    north_turtle = turtle.Turtle()
    south_turtle = turtle.Turtle()

    # Set headings
    north_turtle.setheading(90)
    south_turtle.setheading(270)

    # Draw lines
    north_turtle.forward(distance)
    south_turtle.forward(distance)


def draw_x_axis(distance: int):
    east_turtle = turtle.Turtle()
    west_turtle = turtle.Turtle()

    # Set headings
    east_turtle.setheading(0)
    west_turtle.setheading(180)

    # Draw lines
    east_turtle.forward(distance)
    west_turtle.forward(distance)


if __name__ == "__main__":
    main()
