def fun(fname):
    with open(fname,"r") as myfile:

        data= myfile.readline()
        print(data)
    
fun("student.txt")