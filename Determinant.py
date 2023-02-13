# Determinant
# can also be done with numpy
# recursion will have memory limitations to consider for n is very large


def determinant(m):
	
	if (len(m)==1):
		return m[0][0]
	
	a=0
	for n in range(len(m)):
		a+=(1 if n%2 ==0 else -1)*m[0][n] * determinant([o[:n]+o[n+1:] for o in m[1:]])
	return a
		
	
    
    
m1 = [[4, 6], [3,8]]
m5 = [[2,4,2],[3,1,1],[1,2,0]]

print(determinant(m1))
print(determinant(m5))
