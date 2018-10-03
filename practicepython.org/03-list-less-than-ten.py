#!/user/bin/env python

# author: Mailen Bilsky
# date: 03/10/2018

# title: List Less Than Ten
# url: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# time complexity: O(n), with n being the amount of numbers in the input string

def less_than_5(lst):
	"""
	Take a list, say for example this one:

	  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	and write a program that prints out all the elements of the list that are less than 5.
	"""

  for i in lst:
    if i < 5:
      print(i)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_5(a)
