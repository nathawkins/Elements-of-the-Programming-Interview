##Function to convert base 10 to base 2
def dec_to_bin(number):
    return int(bin(number)[2:])

##Function to convert bin to decimal
def bin_to_dec(number):
    return int(str(number), 2)

##Function to find the weight of a number equal to the number of
##1's in the base 2 number
def get_weight(number):
    bits = list(str(dec_to_bin(number)))
    ones = [x for x in bits if x == '1']
    return len(ones)

##Return a number with the same weight that mimimizes the difference |x-y|
def return_y(x):
    weight_to_match = get_weight(x)
    max_length = 2*len(list(str(dec_to_bin(x)))) ##Assume upper limit on
                                                 ##comparator based on bits

    '''
    I decided to check numbers up until the max length of the binary number x2.
    This serves as a failsafe. The other condition is to do a minimization search.
    Find the difference, and if this_difference is smaller, store it, but if it
    starts getting bigger, stop. This is like traversing down a curve and then stopping
    once we have to start climbing up.
    But, the key in starting to make this more efficient is where to start.
    For a given number, I will take the binary number and strip the zeros.
    The starting point for my loop will then be the decimal number that is formed
    from all of those 1's put together. For example, 6 = (110)_2. So I will start
    the loop at (11)_2 = 3. Not hugely important for small numbers, but very important
    for bigger numbers.
    '''
    ones = [x for x in list(str(dec_to_bin(x))) if x == '1']

    num = bin_to_dec(int(''.join(ones)))

    keep_going = True
    difference = 1E10 ##set arbitrary upper threshold for the difference to start
    result = 0

    while keep_going:
        ##x cannot equal y
        if num == x:
            num += 1
            continue

        ##If the weights are the same
        this_weight = get_weight(num)
        if this_weight == weight_to_match:
            ##Minimize the difference between them
            this_difference = abs(num - x)
            if this_difference < difference:
                result = num
                difference = this_difference

            ##if the difference is going the other way and getting bigger, stop
            if this_difference > difference:
                keep_going = False

        ##failsafe condition, set some max length to stop if it won't find a solution
        if len(list(str(dec_to_bin(num)))) > max_length:
            keep_going = False

        num += 1

    return result

##test cases
print(return_y(6))
print(return_y(92))
print(return_y(319))
print(return_y(6789))
print(return_y(99743))
print(return_y(100003))
