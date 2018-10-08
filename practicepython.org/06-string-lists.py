#!/user/bin/env python

# author: Mailen Bilsky
# date: 08/10/2018

# title: String Lists
# url: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

"""
Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.)
"""


def palindrome_or_not(string):
    """
    :param nmultiply: A string given by the user
    :type multiply: string
    :return: Print a message saying if the string is a palindrome or not
    :rtype: string
    """
    string_lower = string.lower()
    string_reverse = ""
    i = len(string) - 1
    while i >= 0:
        string_reverse += string_lower[i]
        i -= 1
    if string_lower == string_reverse:
        print("Your string is a palindrome!")
    else:
        print("Your string is not a palindrome.")


string = input("Please write a string: ")

if __name__ == '__main__':
    palindrome_or_not(string)
