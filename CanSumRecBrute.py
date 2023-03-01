'''
can the numbers in an array be summed to rach a particular number

inputs
[list of ints]
target int

if the contents of a list can be summed to the target
return True

'''


def canSum(nums,tgt):
	
	# base case
	if tgt ==0:
		return True
	if tgt <0:
		return False
	for num in nums:
		remainder = tgt - num 
		if canSum(nums,remainder) == True:
			return True
	return False






nums = [2,3]
target = 7
print(canSum(nums,target))
