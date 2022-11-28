import linecache

fname = input("enter the file name: ")
num_lines = 0

with open(fname,"r") as f:
    for line in f:
        num_lines += 1

print("number of lines :")
print(num_lines)



n = int(input("enter the last lines :"))

for i in range(num_lines,num_lines-n,-1):
    print(linecache.getline("student.txt",i),end="")



