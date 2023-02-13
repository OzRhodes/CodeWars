# codewars RGB
# convert a 3 decimal digit code into a single Hex string
# h = hex(d)



def rgb(r,g,b):	
	if r > 255:
		r = 255
	if g>255:
		g=255
	if b>255:
		b=255
    
	if r < 0:
		r = 0
	if g<0:
		g=0
	if b<0:
		b=0
	
	r=str(hex(r)).upper()[2:]
	g=str(hex(g)).upper()[2:]
	b=str(hex(b)).upper()[2:]
	if len(r)==1:
		r = "0"+r
	
	if len(g)==1:
		g = "0"+g
	
	if len(b)==1:
		b = "0"+b
	
	

print(rgb(255, 255, 255)) # returns FFFFFF
print(rgb(255, 255, 300)) # returns FFFFFF
print(rgb(0,0,0)) # returns 000000
print(rgb(148, 0, 211)) # returns 9400D3

'''
Best Refactored

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
'''
