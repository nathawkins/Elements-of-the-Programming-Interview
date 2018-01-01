##Function to take in a number and return either a string or integer of the
##reverse. EX: 1234 -> 4321
def reverse(number, return_type = 'str'):
    if return_type == 'str':
        reverse = ''
        digits = list(str(number))
        if digits[0] == '-':
            reverse += '-'
            digits.remove('-')

        reverse += ''.join(digits[::-1])
        return reverse
    if return_type == 'int':
        reverse = ''
        digits = list(str(number))
        if digits[0] == '-':
            reverse += '-'
            digits.remove('-')
        if digits[-1] == '0':
            digits.pop(-1)
        reverse += ''.join(digits[::-1])
        return int(reverse)
    else:
        raise TypeError("Please specify whether you want to return an integer or string.")


print(reverse(314159265838275, return_type = 'int'))
print(reverse(1020, return_type = 'int'))
print(reverse(-238271))

##Function to test whether or not a number is a palindrome
def is_palindrome(number):
    if number < 0:
        return False
    digits = list(str(number))

    if digits == digits[::-1]:
        return True
    else:
        return False

print(is_palindrome(0))
print(is_palindrome(1))
print(is_palindrome(7))
print(is_palindrome(11))
print(is_palindrome(121))
print(is_palindrome(333))
print(is_palindrome(2147447412))
print(is_palindrome(-1))
print(is_palindrome(12))
print(is_palindrome(100))
print(is_palindrome(2147483647))
