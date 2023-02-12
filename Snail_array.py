# the nxn array cann be navigated by following the path of outer ring inwards 
#creating a path which is c to be described as an array

	
def snail(snail_map):
    results = []
    while len(snail_map) > 0:
        # top column
        results += snail_map[0]
        del array[0]

        if len(snail_map) > 0:
            # right column
            for i in snail_map:
                results += [i[-1]]
                del i[-1]

            # borrom column
            if snail_map[-1]:
                results += snail_map[-1][::-1]# reverses the array
                del snail_map[-1]

            # left column
            for i in reversed(snail_map):
                results += [i[0]]
                del i[0]

    return results
	
array = [[1]]

print(snail(array))

'''
import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m
'''
 
