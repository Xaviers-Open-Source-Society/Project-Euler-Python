sum_internal = 0
sum = 0
for number in range(10,1000000):
    for digit in str(number):
        sum_internal = sum_internal + pow(int(digit), 5)
    if sum_internal == int(number):
        sum = sum + int(number)
    sum_internal = 0
print(sum)
