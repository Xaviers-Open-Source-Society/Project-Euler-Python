sum_first = 0
sum_second = 0
sum_amicable = 0
for i in range(1, 10001):
    for j in range(1, i):
        if i % j == 0 and j <= int(i/2):
            sum_first = sum_first + j
    for k in range(1, sum_first+1):
        if sum_first % k == 0 and k <= int(sum_first/2):
            sum_second = sum_second + k
    if sum_second == i and i !=  sum_first:
        print(sum_first, sum_second, i)
        sum_amicable = sum_amicable + i
    sum_first = 0
    sum_second = 0
print(sum_amicable)
