client_name=int(input("please enter, 1 for chinmay, 2 for tanmay, 3 for rutuja\n"))#append version
D= int(input("please enter 1 for diet and 2 for exercise\n"))
def getdate():
    import datetime
    return datetime.datetime.now()
a=getdate()

a=str(a)

if D == 1:
    if client_name == 1:
        f = open("Chinmaydiet.txt", "a")
        f.write("[")
        f.write(a)
        f.write("]")
        f.write(" ")
        f.write(input("what did you eat"))
    if client_name == 2:
        f = open("Tanmaydiet.txt", "a")
        f.write("[")
        f.write(a)
        f.write("]")
        f.write(" ")
        f.write(input("what did you eat\n" ))
    if client_name == 3:
        f = open("Rutujadiet.txt", "a")
        f.write("[")
        f.write(a)
        f.write("]")
        f.write(" ")
        f.write(input("what did you eat"))

if D == 2:
    if client_name == 1:
        f = open("Chinmayexercise.txt", "a")
        f.write("[")
        f.write(a)
        f.write("]")
        f.write(" ")
        f.write(input("what exercise did you did?"))
    if client_name == 2:
        f = open("Tanmayexercise.txt", "a")
        f.write("[")
        f.write(a)
        f.write("]")
        f.write(" ")
        f.write(input("what exercise did you did?"))
    if client_name == 3:
        f = open("Rutujaexercise.txt", "a")
        f.write("[")
        f.write(a)
        f.write("]")
        f.write(" ")
        f.write(input("what exercise did you did?"))
f.close()

