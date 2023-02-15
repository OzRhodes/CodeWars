


def dbl_linear(n) : 
    list = [1] 
    a = 0
    b = 0
    
    while(len(list)<=n) : 
        y = 2*list[a] + 1 
        z = 3*list[b] + 1 
        
        if y>z : 
            list.append(z)
            b+= 1 
        elif y<z : 
            list.append(y)
            a += 1 
        else : 
            list.append(y)
            a += 1 
            b += 1
        print(list)
    return list[n]
print(dbl_linear(5))


'''
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex:  u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:

Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
'''
