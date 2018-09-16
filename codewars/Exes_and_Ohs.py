#!/user/bin/env python

# author: Mailen Bilsky
# date: 11/09/2018

# title: Exes and Ohs
# url: https://www.codewars.com/kata/55908aad6620c066bc00002a
# difficulty: 7 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def xo(s):
  """
  Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean 
  and be case insensitive. The string can contain any char.

  :param nmultiply: String with "x"s and "o"s
  :type multiply: string
  :return: True or False
  :rtype: bool
  """

  x = 0
  o = 0
  for i in s:
    if i == "x" or i == "X":
      x += 1
    elif i == "o" or i == "O":
      o += 1
  if x == o:
    return True
  else:
    return False  