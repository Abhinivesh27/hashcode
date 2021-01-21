input_string = input("Input String: ") #string input
list = []                              #initializing an empty list
j = 1                                  #asign value 1 to j
for i in range(0,len(input_string)-1): #itrating i in range of values starting from 0 to lenght of input_string-1
    list.append((ord(input_string[i])*(31**(len(input_string)-j)))) #this statement will be executed until i reaches its maximum value(length of input_string-1)
    j+=1                               #the value of j will be incremented by 1 for every itration
    
print("Hash: ",sum(list)+ord(input_string[len(input_string)-1])) #prints the final Hash 
