a=21
i=1
while(i<=5):
	inp=int(input("Guess the number:"))
	rem=5-i
	print("attempts remaining=",rem)
	i=i+1
	if inp<a:
		print("the number is lesser\n")
	elif inp>a:
		print("the number is greater\n")
	elif inp==a:
		print("Your guess is correct")
		break
if not inp==a:
	print("game over")
	