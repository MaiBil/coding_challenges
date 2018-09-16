#!/user/bin/env python

# author: Mailen Bilsky
# date: 13/09/2018

# title: Descending Order
# url: https://www.codewars.com/kata/5467e4d82edf8bbf40000155
# difficulty: 7 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def Descending_Order(num):
	"""
	Your task is to make a function that can take any non-negative integer as a argument and return it with its 
	digits in descending order. Essentially, rearrange the digits to create the highest possible number.

	:param nmultiply: Integer
	:type multiply: int
	:return: Integer of input reorganized in descending order
	:rtype: int
	"""

    num1 = str(num)
    num2 = sorted(num1)
    num3 = ""
    i = len(num1) - 1
    while i >= 0:
      num3 = num3 + num2[i]
      i -= 1
    num4 = int(num3)
    return num4