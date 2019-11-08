import random
num_list = []
a = 0
for i in range(1,10):
    num_list.append(i)
print("enter blank spaces with 0,line by line as in row by row")
l1 = list(map(int,input("enter line 1:").split(" ")))
l2 = list(map(int,input("enter line 2:").split(" ")))
l3 = list(map(int,input("enter line 3:").split(" ")))
l4 = list(map(int,input("enter line 4:").split(" ")))
l5 = list(map(int,input("enter line 5:").split(" ")))
l6 = list(map(int,input("enter line 6:").split(" ")))
l7 = list(map(int,input("enter line 7:").split(" ")))
l8 = list(map(int,input("enter line 8:").split(" "))) 
l9 = list(map(int,input("enter line 9:").split(" ")))
grid = [l1,l2,l3,l4,l5,l6,l7,l8,l9]
grid_ch = grid
grid_a = []
for i in range(0,9):
    grid_a.append(num_list)
print(grid_a[1])
while a == 0:    
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] != 0:
                tempplace = grid_a[x].index(grid[x][y])
                tempint = grid_a[x][y]
                grid_a[x][y] = grid[x][y]
                grid_a[x][tempplace] = tempint
    a = 1
            
                   
for i in range(0,9):
    print(grid_a[i])



