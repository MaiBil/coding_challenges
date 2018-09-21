#!/user/bin/env python

# author: Mailen Bilsky
# date: 20/09/2018

# title: Good vs Evil
# url: https://www.codewars.com/kata/52761ee4cffbc69732000738
# difficulty: 6 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def goodVsEvil(good, evil):
    """
    Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. 
    Different races will certainly be involved. Each race has a certain worth when battling against others. 
    On the side of good we have the following races, with their associated worth:

    Hobbits: 1
    Men: 2
    Elves: 3
    Dwarves: 3
    Eagles: 4
    Wizards: 10
    On the side of evil we have:

    Orcs: 1
    Men: 2
    Wargs: 2
    Goblins: 2
    Uruk Hai: 3
    Trolls: 5
    Wizards: 10
    Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side 
    of good and compare it with the worth of the side of evil, the side with the larger worth will tend to win.

    Thus, given the count of each of the races on the side of good, followed by the count of each of the races on 
    the side of evil, determine which side wins.

    Input:
    The function will be given two parameters. Each parameter will be a string separated by a single space. Each 
    string will contain the count of each race on the side of good and evil.

    The first parameter will contain the count of each race on the side of good in the following order:

    Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
    The second parameter will contain the count of each race on the side of evil in the following order:

    Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
    All values are non-negative integers. The resulting sum of the worth for each side will not exceed the limit 
    of a 32-bit integer.    

    :param numbers: List with numbers
    :type numbers: list of ints
    :return: Return "Battle Result: Good triumphs over Evil" if good wins, "Battle Result: Evil eradicates all trace of 
    Good" if evil wins, or "Battle Result: No victor on this battle field" if it ends in a tie.
    :rtype: string
    """

  good_list = good.split(" ")
  evil_list = evil.split(" ")
  good_total = int(good_list[0])*1 + int(good_list[1])*2 + int(good_list[2])*3 + int(good_list[3])*3 + int(good_list[4])*4 + int(good_list[5])*10
  evil_total = int(evil_list[0])*1 + int(evil_list[1])*2 + int(evil_list[2])*2 + int(evil_list[3])*2 + int(evil_list[4])*3 + int(evil_list[5])*5 + int(evil_list[6])*10
  if good_total > evil_total:
      return "Battle Result: Good triumphs over Evil"
  elif evil_total > good_total:
      return "Battle Result: Evil eradicates all trace of Good"
  elif good_total == evil_total:
      return "Battle Result: No victor on this battle field"
