age=int(input())
if 1<=age<=100:
	if age<18:
		print("you cannot drive")
	elif age==18:
		print("we will think")
	else:
		print("you can drive")
else:
	print("enter valid age")