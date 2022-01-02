'''
Problem Statement
Write a function that takes in two non-empty arrays of integers. The function should nd the pair of numbers (one from the rst array, one from the second array) whose absolute difference is closest to zero. The function should return an array containing these two numbers, with the number from the rst array in the rst position. Assume that there will only be one pair of numbers with the smallest difference.
Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17] Sample output: [28, 26]

'''
'''
Solution:
Better time complexity can be achieved by sorting the arrays.
Consider the following two arrays: 
A: {1, 2, 11, 15} 
B: {4, 12, 19, 23, 127, 235} 
1. Suppose a pointer a points to the beginning of A and a pointer b points to the beginning of B. The current difference between a and bis 3. Store this as the min. 
2. How can we (potentially) make this difference smaller? Well, the value at bis bigger than the value at a, so moving b will only make the difference larger. Therefore, we want to move a. 
3. Now a points to 2 and b (still) points to 4. This difference is 2, so we should update min. Move a, since it is smaller. 
4. Now a points to 11 and b points to 4. Move b. 
5. Now a points to 11 and b points to 12. Update min to 1. Move b. And so on. 
'''
import sys

array1 = [1, 2, 11, 15]
array2 = [4, 12, 19, 23, 127, 235]
array1.sort()
array2.sort()

ptr1 = 0
ptr2 = 0
min = sys. maxsize

while ptr1 < len(array1) and ptr2 < len(array2):
    f = array1[ptr1]
    s = array2[ptr2]
    curr_min = abs(array1[ptr1] - array2[ptr2])
   
    if (array1[ptr1] < array2[ptr2]):        
        ptr1 += 1
    
    else:        
        ptr2 += 1

    if (curr_min < min):
        min = curr_min
        pair = [f,s]

print(pair)

