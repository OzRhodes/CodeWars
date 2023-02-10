# build a pile of cubes
# return n for the number of cubes that give the same volume as m or return -1

def find_nb(m):
    total = 0 
    cubes = 1
    while total < m:
        total += cubes ** 3
        cubes += 1
        if total == m:
            return cubes - 1
    return -1
    

print(find_nb(9))
