sum = 0
for number in range(0, 1000001):
    if((str(number) == (str(number)[::-1]))):
        #print(number)
        binary_num = "{0:b}".format(number)
        #print(binary_num)
        binary_num_rev = str(binary_num)[::-1]
        #print(binary_num_rev)
        if((binary_num) == (binary_num_rev)):
            sum = sum + number
print(sum)        
    
