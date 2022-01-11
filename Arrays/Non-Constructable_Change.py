'''
Find the smallest positive integer value that cannot be represented as the sum of elements of any subset of a given set. 
The expected time complexity is O(nlogn).
Examples: 
Input:  arr[] = {1, 3, 6, 10, 11, 15};
Output: 2
'''

def nonConstructibleChange(coins):
	change = 0
	a = sorted(coins)

	for i in range(len(a)):

		if (change + 1 < a[i]):
			return(change+1)
			
		else:
			change += a[i]
	return change+1
