'''
Write a function that takes two arrays representing two numbers and returns the
array of their product.
Ex: [1,1] x [1,1] -> [1,2,1]
'''

def multiply_arrays(A1, A2):
    sign = -1 if (A1[0] < 0) ^ (A2[0] < 0) else 1
    A1[0] , A2[0] = abs(A1[0]), abs(A2[0])

    ##flip for convenient indexing
    A1 = A1[::-1]
    A2 = A2[::-1]

    ##keep track of subsequent rows of the multiplication
    factor_to_add = 0
    results = []
    this_row = []

    ##loop through one number
    for j in range(len(A2)):

        ##loop through the next
        for i in range(len(A1)):

            ##performs each multiplication and if the previous had something bigger
            ##than 10, then add that
            this_multplication = A1[i] * A2[j]
            this_multplication += factor_to_add

            ##reset the factor to add
            if factor_to_add != 0:
                factor_to_add = 0

            ##exclude the final index
            if i != len(A1)-1:
                ##do the algorithm and take into account moving the decimal place
                if this_multplication >= 10:
                    factor_to_add += int(this_multplication/10)
                    this_multplication -= int(this_multplication/10)*10

            ##append the multiplication to the result
            this_row.append(this_multplication)

        ##append the result to the results
        results.append(this_row[::-1])
        this_row = [0 for k in range(j+1)]

    total = 0
    ##do the summation
    for result in results:
        R = [str(x) for x in result]
        string = ''.join(R)
        total += int(string)

    ##make it positive or negative
    total *= sign

    ##put it in the proper format to return
    to_return = list(str(total))
    if to_return[0] == '-':
        to_return[0] += to_return[1]
        to_return.pop(1)

    return [int(x) for x in to_return]

print(multiply_arrays([-1,1], [1,9]), -11*19)
print(multiply_arrays([1,2,1], [2,5,6]), 256*121)
print(multiply_arrays([2,5,6], [-1,2,1]), 256*-121)
print(multiply_arrays([1,9,3,7,0,7,7,2,1], [-7,6,1,8,3,8,2,5,7,2,8,7]), 193707721*-76183827287)
