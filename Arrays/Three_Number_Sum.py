'''
Problem Statement - 

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should nd all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array.

Sample input: 
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
'''

array =  [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
result_list = []

def three_number_sum(array,targetSum):

    # sort array using sorted(array) or array.sort() method
    sorted_array = sorted(array)
    # print(sorted_array)

    #Loop over the numbers -2 because we want to have three triplets hence curr number will be -2 the original length
    for i in range(len(sorted_array) - 2):
        left_ptr = i + 1
        right_ptr = len(array) - 1

        # Use while to make sure left ptr remains less than the right, if it exceeds we are done with the current number and move on to the next value in the array(for loop)
        while(left_ptr < right_ptr):
            curr_sum = sorted_array[i] + sorted_array[left_ptr] + sorted_array[right_ptr]

            # If current sum is equal to target then increase left by 1 and decrease right by 1, beacuse we have more numbers and want to make sure we iterate over all the values.
            if (curr_sum == targetSum):
                result_list.append([sorted_array[i] , sorted_array[left_ptr] , sorted_array[right_ptr]])
                left_ptr +=1
                right_ptr -=1
            # If the curr sum is less than target then increase the left ptr by 1, to make sure we get a value more than the curr sum
            elif (curr_sum < targetSum):
                left_ptr += 1

            elif (curr_sum > targetSum):
                right_ptr -= 1
                
    return(result_list)

