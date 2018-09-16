#!/user/bin/env python

# author: Mailen Bilsky
# date: 11/09/2018

# title: Beginner Series #3 Sum of Numbers
# url: https://www.codewars.com/kata/552c028c030765286c00007d
# difficulty: 7 kyu
# time complexity: O(n), with n being the amount of numbers in the input string


def get_sum(a,b):
  """
  Given two integers a and b, which can be positive or negative, find the sum of all the numbers between 
  including them too and return it. If the two numbers are equal return a or b.

  Note: a and b are not ordered!

  :param nmultiply: Two ints
  :type multiply: int, int
  :return: The sum of all the numbers in between the two numbers of the input (them included).
  :rtype: int
  """

  if a < b:
    c = 0
    while a <= b:
      c += a
      a += 1
  else:
    c = 0
    while b <= a:
      c += b
      b += 1
  return c