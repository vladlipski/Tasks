doors = [0]*100

for step in range(1,101):
    for i in range(step - 1,100,step):
        doors[i] = 1 if doors[i] == 0 else 0

print (doors)