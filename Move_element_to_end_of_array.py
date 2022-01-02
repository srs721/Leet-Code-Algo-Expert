'''
Problem-
You are given a list of integers and an integer. Write a function that moves all the instances of that integer to the end of the array and returns
the array.
Input - array = [2,1,3,4,2,2], toMove = 2
Output-
[1,3,4,2,2,2]'''

array = [2,1,2,2,2,3,4,2]
toMove = 2
start = 0
end = len(array) - 1

while start < end:
    if (array[start] == toMove and array[end] == toMove):
        end -= 1
        array[start],array[end] = array[end],array[start]

    elif (array[start] != toMove and array[end] == toMove):
        start += 1
        end -= 1
    
    elif (array[start] == toMove and array[end] != toMove):
        array[start],array[end] = array[end],array[start]
        start += 1
        end -= 1

    elif (array[start] != toMove and array[end] != toMove):
        start += 1

print(array)


'''
More concise solution:
while start < end:
		if (array[start] != toMove):
			start += 1

		elif (array[end] == toMove):
			end -= 1

		else :
			array[start],array[end] = array[end],array[start]    
			start += 1
			end -= 1
print(array)
            
'''


