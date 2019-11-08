t = int(input())
a = [0][0]
k = [0]
k.clear()
l = [0]
for i in range(t):
    k.append(0)
    l = [int(n) for n in input().split()]
    k[i] = l[1]
    a[i] = list(([int(n) for n in input().split()]))
    l.sort(key=int)
    for j in range(len(a[i])):
        if a[i][j] <= a[i][k-1]:
            l[i] += 1
        else:
            break
for h in range(t):
    print(l[h])