'''
Write a function that take an array fo integers in and increments it up by 1.
Write it so that it doesn't have any loss of precision.
Ex: [1, 2, 9] -> [1, 3, 0]
'''

def increment(D):
    ##first thing I will do is flip the list so I can add 1 to the zeroth element
    D = D[::-1]

    ##if it's not enough to round up
    if D[0] < 9:
        D[0] += 1

    else:
        ##handle the first case directly
        D[0] = 0
        D[1] += 1
        ##if it creates a chain effect
        for i in range(1, len(D)-1):
            if D[i] == 10:
                D[i] = 0
                D[i + 1] += 1
            else:
                break

        ##if it's enough to add another decimal point, handle that case
        if D[-1] == 10:
            D[-1] = 0
            D.append(1)

    ##Flip it back
    return D[::-1]

print(increment([2,9,9,9,9,9,9,9,9,9,9,8,9,9,9,9,9]))
print(increment([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]))
print(increment([1,2,9]))
print(increment([1,2,1]))
print(increment([1,2,3,4,2,1,3,4,2,1,2,2,9,9,9]))

import random as r
test = [r.randint(0,9) for x in range(10000)]
print(test, "\n->\n", increment(test))
