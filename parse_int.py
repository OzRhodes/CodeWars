def parse_int(string):
    # split the string on million, thousand, hundredto get a list of segmented values
    value = string.split('million','thousand','hundred')
    digits = {
        'one':1,
        'two':2,
        'three',3,
        'four',4
        
        
        
        
        }
    teens = {

    }
    tens = {

    }
    return # number


input="one"
print(parse_int())

'''
test.assert_equals(parse_int('one'), 1)
test.assert_equals(parse_int('twenty'), 20)
test.assert_equals(parse_int('two hundred forty-six'), 246)'''