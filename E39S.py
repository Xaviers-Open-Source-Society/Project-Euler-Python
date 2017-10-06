maxed_solution = 0
for p in range(3, 1001):
    count_solution = 0
    for a in range(1, p + 1):
        for b in range(1, p - a + 1):
            for c in range(1, p - a - b + 1): 
                if (a + b + c == p):
                    if (pow(a,2) + pow(b,2) == pow(c,2)):
                        count_solution = count_solution + 1
                    elif (pow(a,2) + pow(c,2) == pow(b,2)):
                        count_solution = count_solution + 1
                    elif (pow(b,2) + pow(c,2) == pow(a,2)):
                        count_solution = count_solution + 1
                    else:
                        continue
    if count_solution > maxed_solution:
        maxed_solution = count_solution
        maxed_value = p
print(maxed_solution, maxed_value)
