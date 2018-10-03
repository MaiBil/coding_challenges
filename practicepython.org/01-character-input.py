#!/user/bin/env python

# author: Mailen Bilsky
# date: 02/10/2018

# title: Character Input
# url: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# time complexity: O(n), with n being the amount of numbers in the input string

def get_name_and_age(name,age,number):
	"""
    Create a program that asks the user to enter their name and their age. Print out a message addressed to them 
    that tells them the year that they will turn 100 years old.

	Extras:

	Add on to the previous program by asking the user for another number and printing out that many copies of the 
	previous message. (Hint: order of operations exists in Python)
	Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as 
	pressing the ENTER button)
    """
    year = 2018 + (100 - int(age))
    print(("You will be 100 years old on the year %s. \n" % year)*int(number))

name = input("What's your name?: ")
age = input("How old are you?: ")
number = input("Give me another number: ")
get_name_and_age(name,age)