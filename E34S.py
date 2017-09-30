import math
sum_all = 0
sum_fact_digit = 0
for i in range(10, 1000000):
    for j in str(i):
        sum_fact_digit = sum_fact_digit + math.factorial(int(j))
    if(sum_fact_digit == i):
        print(i)
        sum_all = sum_all + sum_fact_digit
    sum_fact_digit = 0
print(sum_all)
