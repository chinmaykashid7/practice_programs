'''print("select the operator among following")
print("if Addition=A")
print("Subtraction=S")
print("Multiplication=M")
print("Division=D")'''

print("enter numbers")
a=int(input())
b=int(input())
op=input()
if a==45 and b==3 and op =="M":
	print( "555")

elif a==56 and b==9 and op=="A":
	print("77")
elif a==56 and op=="D" and b==6:
	print("4")
else:
	if op =="A":
		c=a+b
		print(c)
	
	if op =="S":
		c=a-b
		print(c)
	
	if op =="M":
		c=a*b
		print(c)
	
	if op =="D":
		c=a/b
		print(c)

	


	
