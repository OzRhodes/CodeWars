# ball drops from a window height h passes a window height 'window' witha bounce coeff of bounce
# coint the passes of window

def bouncing_ball(h, bounce, window):
	if h>0 and h > window and (bounce > 0 and bounce <1):
		win_passes = 1
		while h> window:
			h *= bounce
			if h> window:
				win_passes += 2
		return win_passes
	else:
		return -1
  	


print(bouncing_ball(30, 0.75, 1.5))


'''

def tests():
        testing(, 1)
        testing(3, 0.66, 1.5, 3)
        testing(30, 0.66, 1.5, 15)
        testing(30, 0.75, 1.5, 21)
        
        '''
