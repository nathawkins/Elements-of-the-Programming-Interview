def check_parity(X):
    '''
    Takes an input of a binary number and checks the parity.
    Ex: Input ==> 1101 (int)
        Ouput ==> "Parity = 1" (odd # of 1's)

    Ex: Input ==> 1001 (int)
        Output ==> "Parity = 0" (even # of 1's)
    '''

    #Preporcess the inputs to make an array of the bits
    if type(X) == int:
        bits = list(str(X))

    elif type(X) == str:
        bits = list(X)

    else:
        raise TypeError("Unkown Data Type Given. Please use integer or string of input.")

    ##Use list comprehension to filter out all of the 1's in the input since
    ##we only really need a count of how many there are
    ones = [x for x in bits if x == "1"]

    ##The parity value is the length of the ones array modulus 2. Odd moduli will
    ##have a remainder of 1, and even will have a remainder of 0.
    parity = len(ones)%2

    print("Parity = {}".format(parity))

    return parity

import random as r
from collections import Counter
##For 64 bit numbers
for _ in range(10):
    test_case = ''
    for _ in range(64):
        test_case += str(r.randint(0,1))
    print(test_case)
    print(Counter(list(test_case)))
    check_parity(test_case)

'''
The goal of this problem is to check the parity of a binary number, which only
entails looking at the number of 1's found in the binary number itself. Because the goal
is just a simple count, I don't see the need for any of this complicated bitwise operation
stuff that EPI does. It's useful information, but I find it largely unneccessary.

##EPI solution #1

def parity(x):
    result = 0
    while x:
        result ^= x & 1 ##The ^ is the XOR operation. 0 if both are 1 or both are 0
        x >>= 1         ## x = x with the bits shifted to the right by 1
    return result

##EPI improved solution

def partity_2(x):
    result = 0
    while x:
        result ^= 1
        x &= x-1 #drop the lowest set bit of x (looks at the intersection of
                 #x&(x-1) and gets rid of a bit)
    return result

##Refined solution from EPI

def parity_refined(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
'''
