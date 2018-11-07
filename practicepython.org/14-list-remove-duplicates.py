"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

def using_sets(lst):
  return list(set(lst))


def using_loops(lst):
  no_duplicates = []
  for i in lst:
    if i not in no_duplicates:
      no_duplicates.append(i)
  return no_duplicates


a = [2,1,3,5,1,8,1,3,6,9]
print(using_sets(a))
print(using_loops(a))