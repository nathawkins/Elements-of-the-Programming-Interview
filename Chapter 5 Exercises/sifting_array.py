'''
Write a function that takes in a sorted array and returns the array without
any duplicate values and shifted to the left with additional zeroes added for
what was removed. Ex: [2,3,5,5,7,11,11,11,13] -> [2,3,5,7,11,13,0,0,0]
'''

def filter(array):
    to_return = []

    for i in range(len(array)):
        if array[i] not in to_return:
            to_return.append(array[i])
        else:
            pass

    to_return += [0] * (len(array) - len(to_return))

    print(to_return)
    
    return to_return

filter([2,3,5,5,7,11,11,11,13])

import random as r
test_case = [r.randint(1,100) for x in range(10000)]
print(test_case)
filter(test_case)
