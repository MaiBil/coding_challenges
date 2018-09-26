#!/user/bin/env python

# author: Mailen Bilsky
# date: 26/09/2018

# title: Human Readable Time
# url: https://www.codewars.com/kata/52685f7382004e774f0001f7
# difficulty: 5 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def make_readable(seconds):
    """
    Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59
    The maximum time never exceeds 359999 (99:59:59)

    You can find some examples in the test fixtures.

    :param numbers: int between 0 and 359999
    :type numbers: int
    :return: String with formath "(HH:MM:SS)"
    :rtype: str
    """

    HH = (seconds // (60*60))
    MM = (seconds - (HH*(60*60))) // 60
    SS = (seconds - (HH*(60*60)) - (MM*60))
    if HH < 10:
        HH = "0" + str(HH)
    if MM < 10:
        MM = "0" + str(MM)
    if SS < 10:
        SS = "0" + str(SS)
    return "%s:%s:%s" % (HH, MM, SS)