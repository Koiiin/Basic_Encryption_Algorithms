def gcdExtended(p, q): 
	if p == 0 : 
		return q,0,1
			
	gcdExtended(q%p, p) 
	x1 = q%p
	y1 = p
	
	x = y1 - (q//p) * x1 
	y = x1 
	
	return x, y 
	

p = 26513
q = 32321
x, y = gcdExtended(p, q) 

if (x > y):
	print(y)
else:
	print(x)
	
