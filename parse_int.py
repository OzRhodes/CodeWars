def parse_int(string):
    # Address outliers
    if string == 'zero':
        return 0
    if string == 'one million':
        return 1000000


    # split the string on million, thousand, hundred to get a list of segmented values

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
        }
    teens = {
        'eleven': 11,
        'twelve':12,
        'thirteen':13,
        'fourteen':14,
        'fifteen':15,
        'sixteen':16,
        'seventeen':17,
        'eighteen':18,
        'nineteen':19
    }
    tens = {
        'ten':10,
        'twenty':20,
        'thirty':30,
        'forty':40,
        'fifty':50,
        'sixty':60,
        'seventy':70,
        'eighty':80,
        'ninety':90
    }
    multiplier = {
        'hundred':100,
        'thousand':1000
    }


    number = 0
    # address numbers below 100
    if len(value)==1:
            # address the dash
        if '-' in value[-1]:
            value = value[-1].split('-')
            number += digits[value[1]]
            number += tens[value[0]]
            return number
        number = digits.get(value[0])
        if  number:
                return number
        number = teens.get(value[0])
        if  number:
            return number
        else:    
            return tens.get(value[0])

    if '-' in value[-1]:
        newvalue = value[:-1] + value[-1].split('-')
    else:
        newvalue = value
    
    answer = 0
    for i in range (len(newvalue)):
        if newvalue[i] in digits:
            number +=digits[newvalue[i]]
        if newvalue[i]in tens:
            number += tens[newvalue[i]]
        if newvalue[i] in multiplier:
            number *= multiplier[value[i]]
            answer +=number
            number = 0
    answer += number    
    return answer


#input = 'one million'
#input = 'two hundred forty-six'
#input='one'
#input='thirty'
#input = 'one hundred'
#input = 'seventeen'
#input = 'forty-six'
#input = 'two hundred forty-six'
#input = 'thirty five thousand'
input = 'ninety nine thousand nine hundred ninety nine'
print(parse_int(input))
