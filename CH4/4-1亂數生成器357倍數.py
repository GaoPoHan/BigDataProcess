#Version 1

import random
times3 = 0
times5 = 0
times7 = 0
others = 0
for i in range(1,101):
    flag = False
    randNum = random.randint(1,100)
    print(randNum, end = ' ')
    if randNum % 3 == 0:
        times3 += 1
        flag = True
    if randNum % 5 == 0:
        times5 += 1
        flag = True
    if randNum % 7 == 0:
        times7 += 1
        flag = True
    if flag == False:
        others += 1
print('\times3 = %d, times5 = %d, times7 = %d'%(times3, times5, times7))
print('others = %d'%(others))