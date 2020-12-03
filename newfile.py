i=0
l =int(input('l'))
list=[]

a=input('a')
for m in a:
	list.append(m)
no = input('n')

for x in list:
	if no == x:
		i = i+1
print(i)
#print(list)