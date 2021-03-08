h= input ()
if h[0].isupper() : 
	right = 1 
	wrong = 0
elif h[0] == " " : 
	right = 0 
	wrong = 0
else : 
	wrong = 1 
	right = 0

try :
	for c in range(len(h)) :
		if h[c] == " " : 
				if h[c+1].isupper() :
					right+=1
				else :
					wrong +=1
	print ("right :" ,right , "wrong :" ,wrong)
except : 
	print ("dont enter space EOL")

 # Bui Duc Hien
