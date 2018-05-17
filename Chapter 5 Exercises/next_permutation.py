test = [6,2,1,5,4,3,0]

def next_permutation(test):
    suffix = [test[-1]]
    ind = len(test)-1

    while True:
        if test[ind-1] > test[ind]:
            suffix.append(test[ind-1])
            ind -= 1
        else:
            ind -= 1
            break

    suffix = suffix[::-1]

    if len(suffix) == len(test):
        return []

    to_swap = len(suffix)-1

    while True:
        if suffix[to_swap] > test[ind]:
            temp = suffix[to_swap]
            suffix[to_swap] = test[ind]
            test[ind] = temp
            break
        else:
            to_swap -= 1

    return test[:ind+1]+suffix[::-1]


print(next_permutation([1,0,3,2]))
print(next_permutation(test))
print(next_permutation([3,2,1,0]))
