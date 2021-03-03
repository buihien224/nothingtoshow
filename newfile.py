h= input ()
right = 0
wrong = 0
check = h[0].isupper()
if check == True : right = 1
else : wrong = 1 
for c in range(len(h)) :
	if h[c] == " " : 
		check = h[c+1].isupper()
		if check == True : 
			right+=1
		else : wrong +=1
print ("right : " ,right , "wrong : " ,wrong)
		
		
