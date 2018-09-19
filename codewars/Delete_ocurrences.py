#!/user/bin/env python

# author: Mailen Bilsky
# date: 19/09/2018

# title: Delete occurrences of an element if it occurs more than n times
# url: https://www.codewars.com/kata/554ca54ffa7d91b236000023
# difficulty: 6 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def delete_nth(order,max_e):
	"""
    Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

    :param numbers: List with numbers, number n
    :type numbers: list, int
    :return: Return the first list with each element no more than n times
    :rtype: list
    """

    ls = []
    for i in order:
        if ls.count(i) < max_e:
            ls.append(i)
    return ls