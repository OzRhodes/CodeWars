# sum the 2 lowet numbers in a list

def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]
    
print(sum_two_smallest_numbers([1,5,4,3,6]))
