sum_of_rmax = 0
largest = 0
remainder = 0
for a in range(3,1001):
    for n in range(0, 2001):
        remainder = (pow((a-1), n) + pow((a+1), n)) % pow(a,2)
        if remainder > largest:
            largest = remainder
    sum_of_rmax = sum_of_rmax + largest
    remainder = 0
    largest = 0
print(sum_of_rmax)
