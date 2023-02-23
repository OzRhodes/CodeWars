def parse_int(string):
    # split the string on million, thousand, hundredto get a list of segmented values
    value = string.split()
    digits = {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'zero':0
        }
    teens = {

    }
    tens = {
        'ten':10,
        'twenty':20,
        'thirty':30

    }
    # address the dash

    number = 0
    
    for i in range (len(value)):
        number +=digits[value[i]]

        

    return number


input="one"
print(parse_int(input))

'''
test.assert_equals(parse_int('one'), 1)
test.assert_equals(parse_int('twenty'), 20)
test.assert_equals(parse_int('two hundred forty-six'), 246)'''