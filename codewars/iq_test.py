#!/user/bin/env python

# author: Mailen Bilsky
# date: 15/09/2018

# title: IQ Test
# url: https://www.codewars.com/kata/552c028c030765286c00007d
# difficulty: 6 kyu
# time complexity: O(n), with n being the amount of numbers in the input string


def iq_test(numbers):
    """
    Find out which one of the given numbers differs from the others. One number differs from the others in evenness. 

    :param numbers: String with same parity numbers with the exception of one.
    :type numbers: str
    :return: Return a position of this number. Keep in mind that indexes of the elements start from 1 (not 0)
    :rtype: int
    """
    evenness = [int(x) % 2 == 0 for x in numbers.split(" ")]
  
    # if only one even
    if evenness.count(True) is 1:
        different = True # intruder is the even number
    else:
        different = False # intruder is the odd number

    return evenness.index(different) + 1

