

def top_3_words(text):

    if text == []:
        return list()
    text = text.lower()
    
    text = text.translate({ord(i):'' for i in '"[],().\/:=-&%^$£@!;'})
    word_list = text.split()
    text_set = set(word_list)
    text_list =list(text_set)
    text_dict = {}
    return_list=[]
    for i in range (len(text_set)):
        word = text_list[i]
        text_dict[word] = word_list.count(word)
    value_key_pairs = ((value, key) for (key,value) in text_dict.items())
    sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
    print(sorted_value_key_pairs)
    
    if len(sorted_value_key_pairs)>2:
    	for i in range(3):
    	
    		return_list.append(sorted_value_key_pairs[i][1])
    	return return_list
    		
    if len(sorted_value_key_pairs)>1:
    	for i in range(3):
    		print(i)
    		
    		return_list.append(sorted_value_key_pairs[i][1])
    	return return_list
    if len(sorted_value_key_pairs)>0:
    	for i in range(2):
    		return_list.append(sorted_value_key_pairs[i][1])
    	return return_list


print(top_3_words('  ...  ")'))

'''
test.assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
        test.assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
        test.assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
        test.assert_equals(top_3_words("  , e   .. "), ["e"])
        test.assert_equals(top_3_words("  ...  "), [])
        test.assert_equals(top_3_words("  '  "), [])
        test.assert_equals(top_3_words("  ''  "), [])
        test.assert_equals(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra


'''






