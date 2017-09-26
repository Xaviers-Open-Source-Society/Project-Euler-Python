sum = 0
for i in range(1, 1001):
    sum = sum + pow( i , i)
array_last_10_digits = []
for i in range(10):
    remainder = sum % 10
    array_last_10_digits.append(remainder)
    sum = (sum - remainder) // 10
print(array_last_10_digits) # Printed in reverse order.
