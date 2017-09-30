array_number = []
attach_number = 1
while attach_number < 1000000:
    number = attach_number
    for digit in str(number):
        array_number.append(digit)
    attach_number = attach_number + 1
product = 1
for i in range(len(array_number)):
    if(i == 0 or i == 9 or i == 99 or i == 999 or i == 9999 or i == 99999 or i == 999999):
        product = product * int(array_number[i])
print(product)
