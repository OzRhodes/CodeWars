# string mix from code wars

def mix(s1, s2):
    ch_histogram = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            string = "1" if val1 > val2 else "2" if val2 > val1 else "="
            ch_histogram[ch] = (-max(val1, val2), string + ":" + ch * max(val1, val2))
    return "/".join(ch_histogram[ch][1] for ch in sorted(ch_histogram, key=lambda x: ch_histogram[x]))

print(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")

'''
Note initial attempt with 2 dictionaries failed to be efficient

print(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
print(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
print(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
print(mix("codewars", "codewars"), "")
print(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")

'''
