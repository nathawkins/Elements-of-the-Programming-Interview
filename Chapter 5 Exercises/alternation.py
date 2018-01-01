'''
Write a program that takes an array and rearranges it such that it alternates.
A -> B where B[0] <= B[1] >= B[2] <= B[3]...
'''

def alternate(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse = i%2)

    return A

test = [1,23,42,34,234,23,42,353,46,56,342,34]
print(alternate(test))

import random as r
test_case = [r.uniform(0,1) for x in range(100)]
print(alternate(test_case))
