color = ['red','green','white','black']

with open('student.txt','w') as myfile:
    for i in color:
        myfile.write("%s\n" % i)

contet = open("student.txt")
print(contet.read())