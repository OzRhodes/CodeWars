#correct the order of a string with numbers in the word for the correct order

def order(sentence):
    words = sentence.split()
    output = ['' for word in words]
    for word in words:
        for char in word:
            if char in '123456789':
                output[int(char)-1] = word
    return ' '.join(output)
    
print(order('th1s is2 order5 3the correc4t'))
