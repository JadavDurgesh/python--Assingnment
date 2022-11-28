n = int(input("enter the lines :"))

f=open("student.txt","r")

for i in range(n):

    print(f.readlines())
f.close()