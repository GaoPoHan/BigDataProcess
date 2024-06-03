import random
n1 = random.randint(1,100)
n2 = random.randint(1,100)
while True:
    solution = n1 + n2
    answer = eval(input('%d + %d = '%(n1, n2)))
    if answer == solution:
        print('Correct, you are very good.')
        break
    else:
        print('Wrong answer, try again.')
print('Over')