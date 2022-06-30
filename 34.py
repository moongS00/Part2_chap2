# 100부터 1000사이의 2개의 난수에 대해서 최대공약수와 최소공배수 출력

import random

rnum1 = random.randint(100, 1000)
rnum2 = random.randint(100, 1000)
divisor = []
maxD = 0

for i in range(1, rnum1+1):
    if rnum1 % i == 0 and rnum2 % i == 0:
        divisor.append(i)
        maxD = i

minD = int((rnum1 * rnum2) // maxD)

print(f'rnum1 : {rnum1} \nrnum2 : {rnum2}')
print(f'최대공약수 : {maxD}')
print(f'최소공배수 : {minD}')
