# even , odd

# generate list from two numbers
import time


def input_method():
    # TODO: check which number is smaller
    number1 = int(input("enter a number1"))
    number2 = int(input("enter a number2"))

    inputed_list = []

    while number1 <= number2:
        inputed_list.append(number1)
        number1 += 1

    return inputed_list

# is_even(num): -> bool


def is_even(num):
    return num % 2 == 0

# iterate over list and find even numbers
