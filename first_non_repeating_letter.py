# non repeating letter

# create a list and a subsequent set from the letters in the string, all lowercase
# count each occurence until the count is greater than 2. if there are none return None
# step thru each letter in the list to see if it is the first letter upper of lower case.
# return that letter

def first_non_repeating_letter(string):
	stringLwr = string.lower()
	for letter in stringLwr:
			if stringLwr.count(letter) == 1:
				return string[stringLwr.index(letter)]
			
	return None
	

s1='sTress'

print(first_non_repeating_letter(s1))



'''Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None
'''
'''
Enumerate is also a good option

def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""
'''
