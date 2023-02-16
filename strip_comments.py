def strip_comments(strng, markers):
    output = ''
    #strng.replace("\t", "")
    marked = False
    for char in strng:
        if marked == False:

            if char in markers:
                marked = True
            else:
                output += char
        elif marked == True:
            if char == '\n':
                marked = False
                if strng[-1] != '\n':
                    output = output.rstrip(' ')
                output += '\n'
    if output[-1:] != '\n':
        return output.rstrip()
    else:
        return output
        
# Or

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
