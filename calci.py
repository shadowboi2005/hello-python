this_list = list((2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97))
semi = {6}
for x in this_list:
    for y in this_list:
        if x != y:
            if x * y < 200:
                semi.add(x * y)
add = {12}
for a in semi:
    for b in semi:
        if a + b < 201:
            add.add(a + b)
T = input()
T = int(T)
N = [0,0]
N.clear()
for i in range(0, T):
    q = input()
    q = int(q)
    N.append(q)
for i in range(0, T):
    if N[i] in add:
        print("yes")
    else:
        print("no")

