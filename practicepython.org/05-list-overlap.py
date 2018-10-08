#!/user/bin/env python

# author: Mailen Bilsky
# date: 04/10/2018

# title: List Overlap
# url: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# time complexity: O(n), with n being the amount of numbers in the input string

"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure
this out at this point - we’ll get to it soon)
"""

import random


def common_list(list1, list2):
    """
    :param nmultiply: Two lists consisting of integers
    :type multiply: list, list
    :return: Returns a list containing only the elements
    that are common between the lists (without duplicates)
    by the user
    :rtype: list
    """
    if len(list1) > len(list2):
        ls = list1
    else:
        ls = list2
    return list(sorted(set([x for x in ls if x in list1 and x in list2])))


def random_list():
    """
    :param nmultiply: None
    :type multiply: None
    :return: Generates a list cointaining a random number of
    elements, containing random numbers
    :rtype: list
    """
    return [random.randint(1, 100) for x in range(random.randint(1, 50))]


a = random_list()
b = random_list()

if __name__ == '__main__':
    print(common_list(a, b))
