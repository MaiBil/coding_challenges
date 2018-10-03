#!/user/bin/env python

# author: Mailen Bilsky
# date: 03/10/2018

# title: Divisors
# url: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# time complexity: O(n), with n being the amount of numbers in the input string

def divisors(num):
	"""
	Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
	"""

  	return [x for x in range(1,int(num)+1) if int(num) % x == 0]

num = input("Choose a number: ")
print(divisors(num))