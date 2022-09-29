""" A simple program to compute the Big O analysis"""

from genericpath import exists


def calculate_average(numbers):
    """ Calculate the average given a list of numbers"""
    my_sum = 0
    for number in numbers:
        my_sum += number
    return my_sum / len(numbers)

print(calculate_average([90,33,11,34,11,94]))

def unique_pets(pets):
    """ Get the unique pets from an array of duplicates. """
    existing = []
    for pet in pets:
        if not pet in existing:
            existing.append(pet)
    return existing

my_pets = ["cat","dog","rat","dog","cat", "bird"]
print(unique_pets(my_pets))
print(set(my_pets))
