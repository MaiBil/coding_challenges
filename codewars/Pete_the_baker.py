#!/user/bin/env python

# author: Mailen Bilsky
# date: 28/09/2018

# title: Pete, the baker
# url: https://www.codewars.com/kata/525c65e51bf619685c000059
# difficulty: 5 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def cakes(recipe, available):
    """
    Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

	Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

    :param numbers: Two dictionaries with ingredients and their amounts
    :type numbers: dict, dict
    :return: Maxium number of cakes Pete can bake
    :rtype: int
    """

    list_of_max = []
    for i in recipe:
        if i in available:
            a = available[i] // recipe[i]
            list_of_max.append(a)
        else:
            list_of_max.append(0)
    return min(list_of_max)