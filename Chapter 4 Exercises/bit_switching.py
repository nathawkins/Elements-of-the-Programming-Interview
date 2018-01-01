##Function that switched bits
def switch_bits(X, i, j):
    '''
    Takes a string X as an input and two indices to be switched. Performs
    the switching and returns the newly arranged binary number as a string.
    Strings were used to prevent issues with leading 0's.
    '''
    bits = list(X)[::-1] ##I flip the list because I want the LSB to be index 0
                              ##and the last index to be the MSB

    value_to_switch = bits[i] ##take the bit at index i and keep it

    ##Take the value at bits[j] and move it to bits[i], but make sure
    ##to replace what's at bits[j] with what WAS at bits[i]
    bits[i] = bits[j]
    bits[j] = value_to_switch

    bits = bits[::-1] ##Reflip

    return ''.join(bits)

print('00011010010101', switch_bits('00011010010101', 0, -1))
