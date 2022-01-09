'''
Problem: Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest. 
'''

Solution 1:

array = [2, 1, 5, 2, 3, 3, 4]
curr_index = []
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if (array[i] == array[j]):

            curr_index.append(j)



min_index = min(curr_index)
print(array[min_index])
    

