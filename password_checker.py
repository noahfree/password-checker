# define the names of the files containing the words
files = ["sgb-words.txt", "1000-most-common-words.txt"]
# LENGTH defines a constant for the minimum length of a good password
LENGTH = 8

# GetWordList() reads the words from the files
def GetWordList(file_names):
	data = None
	datasets = []
    # for every name in the files array
	for name in file_names:
        # open the file, read the file, split the contents at the newline
		file = open(name, "r")
		data = file.read().split("\n")
		# add the data to the datasets array
		for word in data:
			datasets.append(word)
		# close the file
		file.close()
    # return the data
	return datasets

# GetUserInput() gets the password string from the user
def GetUserInput():
	string = ""
	while len(string) == 0:
		string = input("\nPlease enter a potential password:\n")
	return string

# GetHashValue() inputs a string and returns the hash value of that string
def GetHashValue(string):
	value = 0
	for i in range(len(string)):
		value += pow(ord(string[i]), 128-i)
	return value

# CompareHashes() takes a string and a hash GetHashValue
# True is returned if the hash value of the string equals the inputted hash value
# False is returned if the hash value of the string does not equal the inputted hash value
def CompareHashes(word_1, string_hash):
	return GetHashValue(word_1) == string_hash

# MinimumLength() returns True if the length of the string is not less than the inputted length
def MinimumLength(length, string):
	return len(string) >= length

# IsInDict() uses the hash functions to find out if the inputted string is in the list of words
def IsInDict(words, string):
	string_hash = GetHashValue(string)
	for word in words:
		if CompareHashes(word, string_hash):
			return True
	return False

# GetDigitIndices() iterates through the string and returns the number of digits contained in GetHashValue
# string as well as their locations, in the form of a list containing an integer and a list of integers
def GetDigitIndices(string):
	count = 0
	indices = []
	for i in range(len(string)):
		if string[i].isnumeric():
			count += 1
			indices.append(i)
	return [count, indices]

# PasswordCheck() is the function which calls the functions defined above
# 	returns True if the password is GOOD or False if it is BAD
def PasswordCheck(words, string):
	if not MinimumLength(LENGTH, string):
		print("\nInput contains fewer than " + str(LENGTH) + " characters.")
		return False

	indices = GetDigitIndices(string)
	if indices[0] > 1:
		return True

	if indices[0] == 0:
		toggle = not IsInDict(words, string)
		if not toggle:
			print("\nInput found in the word list.")
		return toggle

	if indices[1][0] == (len(string) - 1):
		toggle = not IsInDict(words, string[:(len(string)-1)])
		if not toggle:
			print("\nInput contains a common word + an integer less than 10.")
		return toggle

	toggle = not (IsInDict(words, string[:indices[1][0]]) and IsInDict(words, string[(indices[1][0]+1):]))
	if not toggle:
		print("\nInput contains two common words separated by an integer less than 10.")
	return toggle

# Main() performs the necessary operations
def Main():
	# first gets the word list
	words = GetWordList(files)
	# then gets user input
	password = GetUserInput()

	# then, PasswordCheck() is called to see if the input is a good password or not
	if not PasswordCheck(words, password):
		print("BAD PASSWORD")
	else:
		print("\nGOOD PASSWORD")

	# toggle is used to run the program again if the user chooses
	toggle = input("\nWould you like to run the program again? (y/n)\n")
	while toggle != 'y' and toggle != 'Y' and toggle != 'n' and toggle != 'N':
		toggle = input("\n\nWould you like to run the program again? (y/n)\n")

    # if the user inputes 'y' or 'Y', the Main() runs again
	if toggle == 'y' or toggle == 'Y':
		Main()

# call Main()
Main()
