import random
data = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
# count = 0
# 
# 
# row = random.randint(0, len(data)-1)
# 
# col = random.randint(0, len(data[0])-1)
# print(len(data),row,col)
# data[row][col] = 2 if random.randint(0, 1) else 4

available=[]
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == 0:
            available.append((row, col))
print(available)
print(len(data[0]))