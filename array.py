a = [""]
prime_even = [""]
i = 0
temp = 0
prime = False 
while (True):
	inp = input ()
	if not inp:
		print("excape")   # Enter key to quit
		break
	a.append(int(inp))
	i+=1
a.pop(0)
print (a)
b = a 
#find even prime
print ("find even prime ")
for c in a : 
	temp = 0
	for count in range(1, c + 1) : 
		if c % count == 0 :
			temp +=1
	if temp == 2 :
		if c % 2 ==0 :
			prime_even.append(int(c))
prime_even.pop(0)
print (prime_even)
#replace negative with 0 
print(" replace negative with 0 ")
for c in range(len(b)) :
	if b[c] < 0 : b[c] = 0
print (b)
#cau C

