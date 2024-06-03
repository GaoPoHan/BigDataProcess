import random
while True:
    for i in range(1,7):
        randNum = random.randint(1,49)
        print(randNum, end = ' ')
    print()
    again = eval(input('Countinue:1 or quit:0 ---->'))
    if again == 0:
        break
print('Over')