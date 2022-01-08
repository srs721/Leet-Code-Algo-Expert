'''
Problem : Without using split, reverse, reversed

string = "AlgoExpert is the best!"
output = "best! the is Algoexpert"

'''
#O(n) time | O(n) space - where n is the length of string.

def reverseWordsInString(string):
	words = []
	startOfWord = 0

	for i in range(len(string)):		
		character = string[i]

		if character == ' ':
			words.append(string[startOfWord:i])
			startOfWord = i

		elif string[startOfWord] == ' ':
			words.append(' ')
			startOfWord = i

	words.append(string[startOfWord:])

	str1 = reverseList(words)
	reversed_str = ''.join(str1)
	return(reversed_str)

def reverseList(lists):
    start,end = 0,len(lists)-1
    while (start < end):
        lists[start],lists[end] = lists[end],lists[start]
        start += 1
        end -= 1
    return lists