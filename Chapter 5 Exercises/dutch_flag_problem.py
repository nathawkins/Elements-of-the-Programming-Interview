##Write a function that takes an array and a pivot as an argument as sorts the
##array based on the value of the pivot and returns values less than the pivot,
##then equal to the pivot, then greater to the pivot

def dutch_flag(test_case, pivot):
    ##Get the indices for the cases of lss than, equal to, and greater than
    less_than = [i for i in range(len(test_case)) if test_case[i] < pivot]
    equal_to = [i for i in range(len(test_case)) if test_case[i] == pivot]
    greater_than = [i for i in range(len(test_case)) if test_case[i] > pivot]

    ##Combine to form a new order for the test_case
    new_order = less_than + equal_to + greater_than

    ##Return newly sorted array
    return [test_case[j] for j in new_order]

print(dutch_flag([0,1,1,2,2,1,0], 1))
print(dutch_flag(list(range(10))+list(range(10)), 5))
print(dutch_flag([0,1,1,2,2,1,0,3,3], 3))

def dutch_flag_key(test_case, pivot):
    ##Instead of getting indices, now I want the values themselves
    less_than = [k for k in test_case if k < pivot]
    equal_to = [k for k in test_case if k == pivot]
    greater_than = [k for k in test_case if k > pivot]

    ##Sort the arrays using built in method
    less_than.sort()
    equal_to.sort()
    greater_than.sort()

    return less_than + equal_to + greater_than

print(dutch_flag_key([0,1,1,2,2,1,0,3,3], 1))
print(dutch_flag_key([-1,-2]+list(range(10))+list(range(10)), -1))
print(dutch_flag_key(list(range(1000))+list(range(500)), 63))
