#!/user/bin/env python

# author: Mailen Bilsky
# date: 13/09/2018

# title: Split Strings
# url: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
# difficulty: 6 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def solution(s):
  """
  Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number 
  of characters then it should replace the missing second character of the final pair with an underscore ('_').

  :param nmultiply: String of characters
  :type multiply: string
  :return: List of strings of two characters
  :rtype: list
  """

  ls = []
  i = 0
  if len(s) % 2 == 0:
    while i < len(s)-1:
      ls.append(s[i]+s[i+1])
      i += 2
  else:
    while i < len(s)-2:
      ls.append(s[i]+s[i+1])
      i += 2
    ls.append(s[len(s)-1]+"_")
  return ls