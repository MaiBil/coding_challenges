"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
"""

import random


def common_list(list1, list2):
    if len(list1) > len(list2):
        ls = list1
    else:
        ls = list2
    return list(sorted(set([x for x in ls if x in list1 and x in list2])))


def random_list():
    n = random.randint(1,50)
    ls = []
    for i in range(n):
      ls.append(random.randint(1,100))
    return ls


a = random_list()
b = random_list()
print(common_list(a,b))