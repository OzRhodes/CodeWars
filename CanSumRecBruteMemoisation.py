'''
can the numbers in an array be summed to rach a particular number

inputs
[list of ints]

target int

if the contents of a list can be summed to the target
return True

with memoisation

tree depth is len(list of ints)

'''


def canSum(nums,tgt, memo ={}):
	
	# base case
	if tgt in memo:
		return memo[tgt]
	if tgt ==0:
		return True
		
	if tgt <0:
		return False
	for num in nums:
		remainder = tgt - num 
		if canSum(nums,remainder, memo) == True:
			memo[tgt]=True
			return True
			
	memo[tgt]=False
	return False






nums = [7,10]
target = 1000
print(canSum(nums,target))
