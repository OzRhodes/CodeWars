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

works almost correctly but the test code on codewars is incorrect - independely checked
and the index movig isnt working correctly yet
'''

def pyramid_slide(pyramid):
    slide = 0
    sum = pyramid[0][0]
    index = 0

    for i in range(1, len(pyramid)):
        if pyramid[i][index] > pyramid[i][index+1]:
            slide = pyramid[i][index]
            sum +=slide

        else:
            slide = pyramid[i][index+1]
            index +=1
            sum +=slide

    return sum

#print(75+95+47+87+82+75+73+28+83+47+43+73+91+67+98)
pyramid =  [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],]
print(pyramid_slide(pyramid))
