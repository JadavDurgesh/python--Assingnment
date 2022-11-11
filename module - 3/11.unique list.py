lis = [2,2,9,9,5,1,7,6,3,4]

A = []

for i in lis:
    if i not in A:
        A.append(i)
        A.sort()
print(A)




