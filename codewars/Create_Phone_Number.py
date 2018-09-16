#!/user/bin/env python

# author: Mailen Bilsky
# date: 11/09/2018

# title: Create Phone Number
# url: https://www.codewars.com/kata/525f50e3b73515a6db000b83
# difficulty: 6 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def create_phone_number(n):
    """
    Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string 
    of those numbers in the form of a phone number.

    :param nmultiply: List of numbers
    :type multiply: list
    :return: Return the input in a string in telephone format
    :rtype: string
    """


  num1 = "("
  num2 = ") "
  num3= "-"
  for i in n[0:3]:
    num1 = num1 + str(i)
  for i in n[3:6]:
    num2 = num2 + str(i)
  for i in n[6:]:
    num3 = num3 + str(i)
  num = num1 + num2 + num3
  return num