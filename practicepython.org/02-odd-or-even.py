#!/user/bin/env python

# author: Mailen Bilsky
# date: 03/10/2018

# title: Odd or Even
# url: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# time complexity: O(n), with n being the amount of numbers in the input string

"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.
Extras:

2. Ask the user for two numbers: one number to check (call it num) and one
number to divide by (check). If check divides evenly into num, tell that to
the user. If not, print a different appropriate message.
"""


def parity(numb):
    """
    :param nmultiply: One integer, asked to the user
    :type multiply: int
    :return: String printed with message about the parity of the number asked
    :rtype: string
    """

    if numb % 4 == 0:
        print("Your number is a multiple of 4.")
    elif numb % 2 == 0:
        print("The number you chose is even.")
    else:
        print("The number you chose is odd.")


def is_evenly_diveded(dividend, divider):
    """
    :param nmultiply: Two integers, asked to the user
    :type multiply: int, int
    :return: String printed with message saying if the divider divides evenly
    into the dividend or not
    :rtype: string
    """

    if dividend % divider == 0:
        print("Divider divides evenly into dividend.")
    else:
        print("Divider does not divide evenly into dividend.")


parsed = False
while not parsed:
    try:
        numb = int(input("Choose a number: "))
        parsed = True
    except ValueError:
        print('Invalid value!')

if __name__ == '__main__':
    parity(numb)

print()

parsed = False
while not parsed:
    try:
        dividend = int(input("Now choose a number, we'll call it 'Dividend': "))
        parsed = True
    except ValueError:
        print('Invalid value!')

parsed = False
while not parsed:
    try:
        divider = int(input("Choose another number, we'll call it 'Divider: "))
        parsed = True
    except ValueError:
        print('Invalid value!')

if __name__ == '__main__':
    is_evenly_diveded(dividend, divider)
