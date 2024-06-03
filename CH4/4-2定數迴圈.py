import random

count = 1
while count <= 12:
    for i in range(1,6):
        randNum = random.randint(1,49)
        print('%3d'%(randNum), end = ' ')
    print()
    count += 1
print('Over')