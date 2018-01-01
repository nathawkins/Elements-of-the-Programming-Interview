##Function to perform multiplcation bitwise
def multiply(x, y):
    def add(a, b):
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b

        while temp_a or temp_b:
            ak, bk = a&k, b&k
            carryout = (ak&bk) | (ak&carryin) | (bk&carryin)
            running_sum |= ak^bk ^ carryin
            carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)

        return running_sum | carryin

    running_sum = 0
    while x: #Examines each bit of x
        if x&1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

print(multiply(5,3))
print(multiply(3,5))
print(multiply(121, 23600))

##Function to perform division bitwise
def divide(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power
    return result

print(divide(12,5))
print(divide(1243,52))
print(divide(137672,54))

##Function to calculate an exponential bitwise
def power(x,y):
    result, power = 1.0, y
    if y < 0:
        power, x = - power, 1/x
    while power:
        if power & 1:
            result *= x
        x, power = x*x, power >> 1
    return result

print(power(10,3))
print(power(36,14))
print(power(31415, 17))
