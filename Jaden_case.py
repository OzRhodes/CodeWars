# Capitalise every word in a sentence


def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

print(to_jaden_case('A list of words to jaden case'))
