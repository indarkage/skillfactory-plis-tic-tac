# Tic-Tac
import numpy
from numpy import *

# 1 stage
result0 = ''
matr = list(range(4))
for i in range(4):
    matr[i] = list(range(4))

for i in range(4):
    for j in range(4):
        if i > 0 and j > 0:
            matr[i][j] = '-'
        if j == 0:
            matr[i][j] = i

for i in range(4):
    matr[0][0] = ' '

# 2 stage
print('Задание координат через пробел')
num = 9
while num > 0:
    temp1, temp2 = [], []
    if num%2 > 0:
        s0 ='x'
    else:
        s0 = '0'
    a0 = input(f'Ход {s0}:').split()
    matr_i = int(a0[0])
    matr_j = int(a0[1])
    for i in range(1, 4):
        for j in range(1, 4):
            matr[matr_i][matr_j] = s0

    for i in range(1, 4):
        temp1.append(matr[i][i])
        temp2.append(matr[i][4-i])

    temp3, temp4 = [], []
    temp3.append(matr[:][matr_j])
    matr2 = numpy.array(matr)

    for i in range(1, 4):
        if list(matr2[:, i]).count('0') == 3:
            result0 = 'Победа 0'
        if list(matr2[:, i]).count('x') == 3:
            result0 = 'Победа Х'
        for j in range(1, 4):
            if matr[i].count('0') == 3 or temp1.count('0') == 3 or temp2.count('0') == 3:
                result0 = 'Победа 0'
            if matr[i].count('x') == 3 or temp1.count('x') == 3 or temp2.count('x') == 3:
                result0 = 'Победа Х'

    for row in range(4):
        print(*matr[row])

    if result0 != '':
        print(result0)
        break
    num -= 1
else:
    print('Ничья')
