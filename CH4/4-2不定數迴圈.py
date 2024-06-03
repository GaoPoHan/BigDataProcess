import random
again = 1
while again == 1:
    for i in range(1,7):
        randNum = random.randint(1,49)
        print('%3d'%(randNum), end = ' ')
    print()
    again = eval(input('Countinue:1 or quit:0 ---->'))
print('Over')