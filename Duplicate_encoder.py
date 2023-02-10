#  create a string where each duplicated character becomes '(' and others become ')'
def duplicate_encode(word):

    word = word.upper()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("
            
    return result
    
print(duplicate_encode('abbcdde'))
