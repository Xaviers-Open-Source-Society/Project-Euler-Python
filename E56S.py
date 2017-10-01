sum_digits = 0
largest = 0
for a in range(1,100):
    for b in range(1,100):
        sum_digits = sum(int(digit) for digit in str(pow(a,b)))
        if(sum_digits > largest):
            largest = sum_digits
print(largest)
