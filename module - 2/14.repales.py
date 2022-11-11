str1 = "hello"

print(str1[0:1])
print(str1[0:2])
print(str1[0:3])
print(str1[1:2])
print(str1[1:3])
print(str1[2:3])

subs = []

for i in range(0,len(str1)):
    for j in range(i+1,len(str1)+1):
        subs.append(str1[i:j])

print(subs)