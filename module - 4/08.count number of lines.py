with open("student.txt",'r') as fp:

    lines = len(fp.readline())
    print("total number of lines :",lines)