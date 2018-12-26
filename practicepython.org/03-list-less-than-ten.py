#!/user/bin/env python

# author: Mailen Bilsky
# date: 03/10/2018

# title: List Less Than Ten
# url: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are
less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all
the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements
from the original list a that are smaller than that number given by the
user.
"""


def less_than_num(lst):
    """
    :param less_than_num: A list
    :type less_than_num: list
    :return: Returns a list with all the elements from the input list that
    are smaller than the number given by the user
    :rtype: string
    """
    while True:
        try:
            num = int(input("Choose a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    return [x for x in lst if x < num]


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

if __name__ == '__main__':
    print(less_than_num(a))
