n,m=map(int,input().split())
password=input().split()
password.sort()
answer=[]

def back_tracking():
	
	if len(answer)==n:

		con=0
		vow=0
		for word in answer:
			if word in ['a','e','i','o','u']:
				vow+=1
			else: 
				con+=1

		if vow>=1 and con>=2:
			print(''.join(answer))
		
	else:
    
		for word in password:
			if len(answer)==0:
				answer.append(word)
				back_tracking()
				answer.pop()
			elif answer[-1]<word :
				answer.append(word)
				back_tracking()
				answer.pop()
	
back_tracking()