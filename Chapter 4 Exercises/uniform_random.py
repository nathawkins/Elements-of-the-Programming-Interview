##Function to generate random numbers from some lower bound to some upper
##bound
import random as rand
from collections import Counter
def random(lower, upper):
    number_of_outcomes = upper - lower + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | rand.randint(0,1)
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower

results = []
for _ in range(6000):
    results.append(random(1, 6))
print(Counter(results))
