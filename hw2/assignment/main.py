"""
Phillip Holland
COSC 5340
Summer 2018
Assignment 2
"""


def calculate_paycheck(pay_rate: float, hours_worked: float):
    """ Write a function that takes two parameters:  pay rate,
                                                    number of hours worked
        and returns the pay. Any hours over 40 are paid at time and a half. """

    overtime = 0 if hours_worked <= 40 else hours_worked - 40
    straight_time = 40 if hours_worked > 40 else hours_worked

    standard_pay = straight_time * pay_rate
    overtime_pay = overtime * pay_rate * 1.5
    total_pay = standard_pay + overtime_pay

    print(total_pay)


def inCircle():
    """ Write a function inCircle that takes a point and a radius as a parameter.
        The function should return True if the point is inside the circle and False otherwise. """


def plot_all_points():
    """ Modify the simulation to plot points in the entire circle.
        You will have to adjust the calculated value of pi accordingly.
        The program in Helper Programs->Chapter 2 is to help you.
        Test your output multiple times. """


def main():
    calculate_paycheck(10, 100)


if __name__ == "__main__":
    main()
