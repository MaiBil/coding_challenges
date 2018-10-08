#!/user/bin/env python

# author: Mailen Bilsky
# date: 08/10/2018

# title: List Comprehensions
# url: https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16,
25, 36, 49, 64, 81, 100]. Write one line of Python that takes this
list a and makes a new list that has only the even elements of
this list in it.
"""


def even_list(a):
    """
    :param nmultiply: A list with integers
    :type multiply: list
    :return: Return a list with only the even numbers of the original list
    :rtype: list
    """
    return [x for x in a if x % 2 == 0]


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

if __name__ == '__main__':
  print(even_list(a))