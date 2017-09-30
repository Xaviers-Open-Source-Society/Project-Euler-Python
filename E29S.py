array_powers = []
for a in range(2, 101):
    for b in range(2, 101):
        array_powers.append(pow(a, b))
array_powers_set = {power for power in array_powers}
print(len(array_powers_set))
