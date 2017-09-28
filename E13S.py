array_file = []
with open('E13.txt') as file: #save the number as it is in a txt file.
    for line in file:
        array_file.append(line)
sum = 0
for number in array_file:
    if number == '\n':
        sum = sum
    else:
        sum = sum + int(number);
counter = 0                 #counting the first 10 digits
for digit in str(sum):
    if counter < 10:
        print(digit, end = '')
    else:
        continue
    counter = counter + 1

