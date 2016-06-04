import itertools from *
def threeSum(nums):
	l = []
	com = combinations(nums,3)
	for i in com:
		if sum(i) == 0:
			l.append(i)
	return l		
