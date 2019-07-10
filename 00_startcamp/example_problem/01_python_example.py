import random

numbers = range(1,10)
Input = random.choice(numbers)

x = Input * 11
y = Input * 111
z = Input * 1111
Output = Input + x + y+ z
print(f' {Input}, {Output}')