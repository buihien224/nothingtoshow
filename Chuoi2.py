h= input ()
if h[0].isupper() == True : right = 1 ; wrong = 0
else : wrong = 1 ; right = 0
for c in range(len(h)) :
	if h[c] == " " : 
		if h[c+1].isupper() == True : right+=1
		else : wrong +=1
print ("right : " ,right , "wrong : " ,wrong)
		
