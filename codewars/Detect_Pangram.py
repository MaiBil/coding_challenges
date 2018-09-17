#!/user/bin/env python

# author: Mailen Bilsky
# date: 17/09/2018

# title: Detect Pangram
# url: https://www.codewars.com/kata/545cedaa9943f7fe7b000048
# difficulty: 6 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

import string

def is_pangram(s):
	"""
    A pangram is a sentence that contains every single letter of the alphabet at least once. For example, 
    the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters 
    A-Z at least once (case is irrelevant).

	Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore 
	numbers and punctuation.

    :param numbers: String with text
    :type numbers: str
    :return: Return true if string is a pangram
    :rtype: bool
    """

    a = "abcdefghijklmnopqrstuvwxyz"
    b = ""
    for x in a:
        if x in s.lower():
        	b += x
    if b == a:
        return True
    else:
        return False
