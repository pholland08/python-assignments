"""
Phillip Holland
COSC 5340
Summer 2018
Assignment 2
"""

import math
import turtle


def calculate_paycheck(pay_rate: float, hours_worked: float):
    """ Write a function that takes two parameters:  pay rate,
                                                    number of hours worked
        and returns the pay. Any hours over 40 are paid at time and a half. """

    overtime = 0 if hours_worked <= 40.0 else hours_worked - 40.0
    straight_time = 40 if hours_worked > 40.0 else hours_worked

    standard_pay = straight_time * pay_rate
    overtime_pay = overtime * pay_rate * 1.5
    total_pay = standard_pay + overtime_pay

    return total_pay


def inCircle(point: (float, float), radius: float):
    """ Write a function inCircle that takes a point and a radius as a parameter.
        The function should return True if the point is inside the circle and False otherwise. """

    hyp = math.hypot(point[0], point[1])

    if radius < 0 or hyp > radius:
        return False

    return True


def plot_all_points(radius: int):
    """ Modify the simulation to plot points in the entire circle.
        You will have to adjust the calculated value of pi accordingly.
        The program in Helper Programs->Chapter 2 is to help you.
        Test your output multiple times. """

    turtle.tracer(0, 0)

    ts = turtle.Screen()
    ts.bgcolor("red")

    t = turtle.Turtle()
    t.color("green")
    t.speed(10)
    t.up()

    for x in range(-2*radius, 2*radius, 1):
        for y in range(-2*radius, 2*radius, 1):
            if inCircle((x, y), radius):
                plot_point(t, (x, y))

    turtle.update()
    t.hideturtle()
    ts.exitonclick()


def plot_point(t: turtle.Turtle, point: (float, float)):
    t.goto(point[0], point[1])
    t.dot(.01)


def main():
    calculate_paycheck(10, 100)
    inCircle((3, 4), 5)
    plot_all_points(100)


if __name__ == "__main__":
    main()
