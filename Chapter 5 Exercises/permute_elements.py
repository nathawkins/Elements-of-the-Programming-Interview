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
