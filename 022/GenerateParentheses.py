def func(i,rtn):
	foo ={} 
	for s in rtn:
		for j in xrange(0,i*2):
		    if j != 0 and s[j-1] == ')':
		        continue
		    foo['('+s[0:j]+')'+s[j:]] = 1 
	return list(foo.keys())
def generateParenthesis( n):
	rtn = ['()']
	for i in xrange(1,n):
		rtn = func(i,rtn)
	return rtn

print(generateParenthesis(1))
print(generateParenthesis(2))
print(generateParenthesis(3))
print(generateParenthesis(4))
print(generateParenthesis(5))
print(generateParenthesis(6))
