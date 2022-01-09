'''
You’re given an array of integers where each integer represents a jump of its value in an array. For instance, the integer 2 represents a jump of two indices forward in the array; the integer -3 represents a jump of three indices backward in the array.
If a jump spills past the array’s bounds, it wraps over to the other side. For instance, a jump of -1 at index 0 brings us to the last index in the array. Similarly, a jump of 1 at the past index in the array brings us to index 0.
Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle occurs if, starting at any index in the array and following the jumps, every element is visited exactly once before landing back on the starting index.
'''

'''
Solution:

Single cyclic check means visitng each vertex exactly once and forms a cycle.

Considering this, there are three conditions we need to track.
We need to visit n number of elements where n = array.length
If, after we have visited every element, we are not back at the starting point, we have a problem
If we have visited more than one element, and not yet visited every other element (1<n<array.length), and we find ourselves back at the starting point, we have a problem
'''


def hasSingleCycle(array):
	visited = 0
	currentIdx = 0
	while visited <len(array):
		if visited > 0 and currentIdx == 0: # To check if we have visited more than 1 element and we end up at index 0, means we have multiple cycles.
			return False 
		visited += 1
		currentIdx = nextjump(currentIdx, array)
	return currentIdx == 0
		
def nextjump(currentIdx, array):

	jump = array[currentIdx]
	nextjump = (currentIdx + jump) % len(array) #To wrap around the array
	return nextjump if nextjump >= 0 else nextjump+len(array) #to make sure we are returning equivalent of a negative number.