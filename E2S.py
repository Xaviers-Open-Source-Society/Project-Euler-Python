fib1 = 1
fib2 = 2
fibn = 0
sum_even_fibn = 0
while fibn <= 4000000:
    fibn = fib1 + fib2
    if(fib2 % 2 == 0):
        sum_even_fibn = sum_even_fibn + fib2
    fib1 = fib2
    fib2 = fibn
print(sum_even_fibn)
