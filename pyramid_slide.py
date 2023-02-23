'''
imagine a pyramid of numbers

        3
       7  4
     2  4  6
   8  5   9  3

moving down the pyramid
what is the largest sum adding a number for each row that is a fork of the row above.

as you step down you move left of right checking for the max of 2 numbers
using slicing to identify the next 2 numbers to compare
'''

def pyramid_slide(pyramid):
    sum = 0
    for i in range(len(pyramid)):
        sum += max(pyramid[i])
    return sum




pyramid = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
print(pyramid_slide(pyramid))