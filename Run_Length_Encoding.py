string = "AAAAAAAAAAAAABBCCCCDD"
length = 1
chars = []
res = ''

for i in range(len(string)-1):

    if (string[i] == string[i+1]): #If the next character is equal increement length
        length += 1
        if length == 9:  #To check if the length exceeds 9 then append the run length and assign length to 0
            chars.append(length)
            chars.append(string[i])
            length = 0
        if i+2 == len(string): #To handle last iteration and append the last run length to chars array
            chars.append(length)
            chars.append(string[i - 1])
    else:
        chars.append(length)   #Add the run length to char array if the first if conditions fails and initialise length to 1 
        chars.append(string[i])
        length = 1



res = ''.join(str(char) for char in chars) #Convert chars array to string
print(res)
