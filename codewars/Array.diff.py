#!/user/bin/env python

# author: Mailen Bilsky
# date: 12/09/2018

# title: Array.diff
# url: https://www.codewars.com/kata/523f5d21c841566fde000009
# difficulty: 6 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def array_diff(a, b):
	"""
    Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

	It should remove all values from list a, which are present in list b.

	array_diff([1,2],[1]) == [2]
	If a value is present in b, all of its occurrences must be removed from the other:

	array_diff([1,2,2,2,3],[2]) == [1,3]

    :param nmultiply: Two lists with numbers
    :type multiply: list
    :return: New list with all values from list a which are present in list b removed
    :rtype: list
    """

    c = []
    for i in a:
      if i not in b:
        c.append(i)
    return c