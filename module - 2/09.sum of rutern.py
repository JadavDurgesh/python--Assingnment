def sum(a,b):

    sum=a+b

    if sum in range(12, 18): # 10+5 = 15 rigth answer.... | # 10 + 6 = 16 rong answer....to print the sum is 16 up
        return "12 to 18 teen age.."

    else:
        return sum

print(sum(10, 6))
print(sum(2, 5))
print(sum(12, 15))