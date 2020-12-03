dict= {"foopish" : "appearance concious",  "natty" : "neatly dressed", "bedizen" : "dressed up in cheap","epaulet" : "ornamental decoration worn on shoulder"}
word=input('word=')
#a=dict[word]
if word in dict:
	print("the meaning is =",dict[word])
else:
	print("word not found")