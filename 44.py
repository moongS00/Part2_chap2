# 카드 7장 중 3장을 선택했을 때 3,4,5가 동시에 선택될 확률은?

n = 7
r = 3

res1 = 1
res2 = 1
res3 = 1

for i in range(1, n+1):
    res1 *= i

for i in range(1, r+1):
    res2 *= i

for i in range(1, n-r+1):
    res3 *= i

com = int( (res2*res3 / res1)  * 100)

print(f'확률 : {com}%')