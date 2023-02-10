# detect pangram
# make the string a set (no duplicates)
# coint the number of alpha numerics
# if 26 then its True otherwith False

def is_pangram(s):
    return len(set(filter(lambda x: x.isalpha(),s.lower()))) == 26
