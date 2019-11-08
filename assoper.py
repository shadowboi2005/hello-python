n = input("no of fibonnaci nos needed")
n = int(n)
n += 1
i = 0
x = [0,1]
print(x)
for i in range(n):
    x.append(i)
    x[i+2] = x[i+1]+x[i]
    print(x[i+2])

