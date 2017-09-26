import math
number = math.factorial(100)
sum = 0
while number != 0:
    remainder = number % 10
    sum = sum + remainder
    number = (number - remainder) // 10
print(sum)
