# 100부터 1000사이의 난수를 소인수분해하고 각각의 소인수에 대한 지수를 출력하자

import random
rNum = random.randint(100, 1000)
prime = []
nNum = rNum

print(f'rNnum : {rNum}')

n = 2
while n <= rNum:
    if nNum % n == 0:
        prime.append(n)
        nNum /= n
    else:
        n += 1

print(f'prime : {prime}')

tempNum = 0
for s in prime:
    if tempNum != s:
        print(f'{s}\'s count : {prime.count(s)}')
        tempNum = s
