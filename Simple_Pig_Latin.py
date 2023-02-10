# Converts text into pig-latin ignoring the punctuation

def pig_it(text):
	text_lst = text.split(' ')
	pig_list = []
	for word in text_lst:
		if word in '!.%&?':
			pig_list.append(word)
		else:
			pig_list.append(word[1:] + word[0] + 'ay')
	return ' '.join(pig_list)

print(pig_it("this is pig latin")) 
