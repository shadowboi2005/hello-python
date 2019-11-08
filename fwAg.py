t = int(input())
x = []
l = 0
d = [0]
r = 1


def recur():
    a = [int(n) for n in input().split()]
    return a


for i in range(t):
    x.append(0)
    N = int(input())
    x[i] = recur()
    for j in range(0, 100000, r):
        x[i].append(-123)
        if x[i][j] != -123:
            for k in range(j):
                l = l + x[i][k]
            r = r + l
            d.append(0)
            d[i] += 1
            if l < N:
                continue
            else:
                break
        else:
            break
print(d)
