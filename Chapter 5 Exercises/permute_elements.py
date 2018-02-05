def permute_array(A, P):
    '''
    Takes in an array of elements, A, and a permutation array, P.
    The index of the permutation array denotes the elemtn of
    A to move, and the value of P at said index is where the element
    is moved to.

    >>> permute_array(["a", "b", "c", "d"], [2, 0, 1, 3])
    ['b', 'c', 'a', 'd']
    '''
    R = [0] * len(A)
    for i, a in enumerate(P):
        this_element = A[i]
        R[a] = this_element

    return R

A = ["a", "b", "c", "d"]
P = [2, 0, 1, 3]
print(permute_array(A, P))

def permute_elements(A, P):
    ##Book's solution for a function that takes up no additional storage space
    ##(i.e. doesn't define a new array to store permutation)
    def cyclic_permutation(start, P, A):
        ##Really all I need
        ##Pick the index to start at, in this case, 0 is a good choice
        ##find the element at the 0th element in the array A
        i, temp = start, A[start]
        while True:
            ##The next index is whatever P[i] is
            next_i = P[i]
            ##The next value that we need to find a place for is A[P[i]]
            next_temp = A[P[i]]
            ##Change the value of A[P[i]]
            A[next_i] = temp
            ##BUT, in th next iteration, we have to find a place for what was at
            ##A[P[i]], so we look at thay index of P and see what the instructions
            ##were for that element
            i, temp = next_i, next_temp
            ##If all of the elements have been taken care of, break
            if i == start:
                break

    for i in range(len(A)):
        j = P[i]
        while j != i:
            if j < i:
                break
            j = P[j]
        else:
            cyclic_permutation(i, P, A)

    return A

print(permute_elements(A, P))
