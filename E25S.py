fib1 = 1
fib2 = 1
length = 1
index = 2
while length != 1000:
    fibn = fib1 + fib2
    index = index + 1
    length = len(str(fibn))
    fib1 = fib2
    fib2 = fibn
print(index)
