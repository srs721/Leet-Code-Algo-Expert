'''
Problem: 
Write a function that takes in non-empty array of integers and returns an array of the same length, where each element in the output
array  is equal to the product of every other number in the input array.

Sample:
a = [5, 1, 4, 2]

Output: [8,40,10,20]
8 = 1*4*2
40 = 5*4*2
10 = 5*1*2
20 = 5*1*4
'''
a = [5, 1, 4, 2]
product_lst = []
for i in range(len(a)):
    prod = 1
    for j in range(len(a)):
        if(i != j):
            prod = prod * a[j]
    product_lst.append(prod)

print(product_lst)