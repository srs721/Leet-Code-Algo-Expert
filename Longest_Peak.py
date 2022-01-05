array = [1, 2, 3, 3, 4, 10, 0, 6, 5, -1, -3, 2, 3]


i = 1
maxlength = 0
while i < len(array) - 1:
    if (array[i-1] < array[i] and array[i+1] < array[i]):
        peak = array[i]
    
    else:
        i += 1
        continue

    #expand left side
    left = i-2

    while left >=0 and array[left] < array[left+1]:
        left -= 1
    
    #expand right side
    right = i+2

    while right <len(array) and array[right] < array[right-1]:
        right+=1

    peak_length = right -left -1

    # maxlength = max(maxlength,peak_length)
    i = right

print(peak_length)



