#!/user/bin/env python

# author: Mailen Bilsky
# date: 24/09/2018

# title: Which are in?
# url: https://www.codewars.com/kata/550554fd08b86f84fe000a58
# difficulty: 6 kyu
# time complexity: O(n2), with n being the amount of numbers in the input string

def in_array(array1, array2):
	"""
	Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of 
	a1 which are substrings of strings of a2.

	#Example 1: a1 = ["arp", "live", "strong"]

	a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

	returns ["arp", "live", "strong"]

	#Example 2: a1 = ["tarp", "mice", "bull"]

	a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

	returns []

    :param numbers: Two lists with string of letters
    :type numbers: list, list
    :return: Return a sorted list with the elements of array1 that are substrings in array2
    :rtype: list
    """

    a = []
    for i in array1:
        for j in array2:
            if i not in a and i in j:
                    a.append(i)
    return sorted(a)