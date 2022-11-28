fruits = {'strawberry':20,'apple':300, 'banana':50, 'papaya':40, ' mango':65}

costly = sorted(fruits,key=fruits.get, reverse=False)

for index in range(2):
    print(costly[index])