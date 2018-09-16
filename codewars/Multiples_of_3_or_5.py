#!/user/bin/env python

# author: Mailen Bilsky
# date: 16/09/2018

# title: Multiples of 3 or 5
# url: https://www.codewars.com/kata/514b92a657cdc65150000006
# difficulty: 6 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def solution(number):
  """
  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

  Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

  Note: If the number is a multiple of both 3 and 5, only count it once.

  :param nmultiply: One number
  :type multiply: int
  :return: One number, consisting of the sum of all the numbers below input that are multiples of 3 or 5
  :rtype: int
  """

  # a is a list with all the numbers below input that are multiples of 3 or 5
  a = [x for x in range(1,number) if x % 3 == 0 or x % 5 == 0]
  return sum(a)