'''
Problem: Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest. 
'''

arr = [2, 1, 5, 2, 3, 3, 4]

i=1
while i < len(arr) -1:
    if(arr[i] == a[i+1]):
        print(index(arr[i]))
        break

