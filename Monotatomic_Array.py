'''
Problem -
The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return “True” if the given array A is monotonic else return “False”
'''

array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
length = len(array) -1
bool_value = False

print(array[-1])
if len(array) == 0 or len(array) == 1:
    bool_value = True

if (all(array[i] <= array[i+1] for i in range(len(array) -1)) or 
		all(array[i] >= array[i+1] for i in range(len(array) -1))):
			bool_value = True

print(bool_value)