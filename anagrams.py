# Owen Wilborn
# anagrams.py

#Finds all direct anagrams of input words compared to a file words.txt imported, solved problem two ways, first by permutation method, second
#second by alphabetical ordering. The main is used to test the two methods to compare.

##################    Functions    ##################
######## Option 1 - Based on permutations #########
#findAnagram1
def findAnagram1(word, dict, results):
	"""
	This function returns all the number of all possilbe Permutations of the input word
	and prints the permutations to the screen
	"""
	swapOne = 0
	swapTwo = 0
	matches = 0
	wordDict = []
	size = setDict(dict, wordDict, len(word));

	matches = swapLetters(word, word, swapOne, swapTwo, len(word), matches, results)
	return matches;

#swapLetters
def swapLetters(orignalWord, word, swapOne, swapTwo, wordSize, matches, results):
	"""
	This function swaps to letters in the input string, and is recursive to find all the possible 
	permutations in the word, if the word is in the dictionary it adds word to results list
	"""
	if wordSize > 0:
		listWord = list(word)
		listWord[swapOne], listWord[swapTwo] = listWord[swapTwo], listWord[swapOne]
		word = ""
		for x in range (0, len(listWord)):
			word+=listWord[x]
	if swapTwo < wordSize-1:
		matches = swapLetters(orignalWord, orignalWord, swapOne, swapTwo+1, wordSize, matches, results)
	if swapOne < wordSize - 2:
		matches = swapLetters(word, word, swapOne + 1, swapOne + 1, wordSize, matches, results)
	if ((swapOne == wordSize - 2 or swapOne == wordSize -1) and not identicalEntry(results, word) and wordInDict(word, dict)):
		matches+=1
		results.append(word)
	return matches

#identicalEntry
#Check for identical entry
def identicalEntry(list, word):
	for x in range (0, len(list)):
		if list[x] == word:
			return True
	return False

#wordInDict
#Check if word is in dictionary
def wordInDict(word, dict):
	for x in range (0 , len(dict)):
		if dict[x] == word:
			return True
	return False

############## Option 2 - Based on alpha ordering of each word's characters ##############
#findAnagram2
def findAnagram2(word, dict, results):
	#First remove all words of bad size
	midDict = []
	setDict(dict, midDict, len(word))
	#Next rearrange all characters in each word in the new dict to be in alphabetical order
	newDict = []
	alphaDict(midDict, newDict)
	#Place input word characters in alphabetical order
	newWord = placeAlpha(word)
	#set matches to zero
	matches = 0
	#For each word see if it is a perfect match
	for x in range (0, len(newDict)):
		if newDict[x]==newWord:
			#if perfect match increase match count and store the original word in the results
			matches=matches+1
			results.append(midDict[x])
	return matches

#alphaDict
#Create new dictionary by arrange characters in each word in alphabetical order
def alphaDict(dict, alphaDict):
	for x in range (0 , len(dict)):
		alphaDict.append(placeAlpha(dict[x]))
	return x

#placeAlpha
#Places word characters in alphabetical order
def placeAlpha(word):
	#If length less than 1 is not a word so return empty string
	if len(word) < 1:
		return ""
	#else turn the word into a string
	listWord = list(word)
	newWord = []
	for x in range (0 , len(word)):
		#Get the next character to add
		character = listWord[x]
		#If string is empty add character to the front
		if len(newWord) < 1:
			newWord.insert(0,character)
		#else find position to find the character
		else:
			for k in range (0, len(newWord)):
				if character < newWord[k]:
					newWord.insert(k, character)
					break
				#at end of the newWord so add at the end
				elif len(newWord) == k+1:
					newWord.insert(len(newWord),character)
	word = ""
	for x in range (0, len(newWord)):
		word+=newWord[x]
	return word

################ Other functions both options use ####################################
#viewArray
def viewArray(list):
	"""
	This function prints all the elements in the list from the first to last index, with each element on a new line
	"""
	for i in range (0 , len(list)):
		print(list[i])
	return

#setDict
def setDict(dict, wordDict, wordSize):
	"""
	Creates a new dict with only the words of matching 
	size from the old dictionary, returns the size of the new dictionary
	"""
	size = 0
	for pos in range (0,len(dict)):
		if len(dict[pos]) == wordSize:
			wordDict.append(dict[pos])
			size = size +1
	return size

##################  Main   ##################

#######  Open dict txt file  ########
dict = []
# open file and read the content in a list
with open('words.txt', 'r') as filehandle:
	filecontents = filehandle.readlines()
	i=1
	for line in filecontents:
		if len(filecontents) != i:
			# remove linebreak which is the last character of the string
			current_place = line[:-1]
		else:
			current_place = line
        # add item to the list
		dict.append(current_place)
		i = i+1
print("Number of words in dictionary", len(dict))

########  Compute for the word   ########
# input
print("Enter word: ", end = "")
word = str(input())

#Option 1 based on permutations
results = []
count1 = findAnagram1(word, dict, results)

# output
print()
print("Solved by permutations method")
print("Word entered is", word)
print("The number of anagrams is", count1, "The anagrams are list below")
viewArray(results)

#Solve second option by alphabetical organization
print()
results = []
count2 = findAnagram2(word, dict, results)
print("Solve by alphabetical organization of word")
print("Word organized:",placeAlpha(word))
print("The number of anagrams is", count2, "The anagrams are list below")
viewArray(results)
print()

#Test to options aganist each other
if count1 == count2:
	print("****Good****")
else:
	print("****Error****")
print()

##################  End Main  ##################
