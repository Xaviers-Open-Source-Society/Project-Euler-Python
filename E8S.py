array_file = []
with open('E8.txt') as file:
    for line in file:
        for number in line:
            if number != '\n':
                array_file.append(number)
product = 1
largest = 1
for i in range(1, 987):
    j = i
    while j < (i + 13):
        product = product * int(array_file[j])
        j = j + 1
    if product >= largest:
        largest = product
    product = 1
print(largest)    
