t = int(input())
a = []
f = 0
for i in range(t):
    n = list(map(int, input().split()))
    k = n[0]
    n.pop(0)
    for j in range(len(n)):
        f = f + n[j]
    if k != 0:
        if f % k <= (k/2) or f % k == ((k/2) - 1):
            a.append(0)
        else:
            a.append(1)
    else:
        a.append(1)
for i in range(t):
    if a[i] == 0:
        print("CHEF")
    else:
        print("COOK")