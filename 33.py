# 100부터 1000사이의 2개의 난수에 대해서 공약수와 최대공약수를 출력하고, 서로소인지 출력
import random

rnum1 = random.randint(100, 1000)
rnum2 = random.randint(100, 1000)
divisor = []
maxD = 0

for i in range(1, rnum1+1):
    if rnum1 % i == 0 and rnum2 % i == 0:
        divisor.append(i)
        maxD = i


print(f'rnum1 : {rnum1} \nrnum2 : {rnum2}')
print(f'공약수 : {divisor}')
print(f'최대공약수 : {maxD}')

if maxD == 1:
    print(f'{rnum1}와 {rnum2}는 서로소')