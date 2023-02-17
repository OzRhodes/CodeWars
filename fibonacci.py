from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
    	return 0
    if n ==1:
    	return 1
    a,b,i = 0,1,0
    while(i<n):
      a,b = b,a+b
      i=i+1
    return a+b
  
print(fibonacci(2))

