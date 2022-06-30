# 100부터 1000사이의 난수에 대해 약수, 소수, 소인수를 출력하는 프로그램
import random
num = random.randint(100, 1000)
divisor = []
prime = []
primeFactor = []

for i in range(1, num+1):
    if num % i == 0:
        divisor.append(i)


for n in range(2, num+1):
    flag = True
    for k in range(2, n):
        if n % k == 0:
            flag = False
            break

    if flag:
        prime.append(n)


newN = num
for j in range(2, num+1):
    if newN % j == 0:
        primeFactor.append(j)
        newN /= j


print('{}의 약수 : {}'.format(num, divisor))
print('{}까지의 소수 : {}'.format(num, prime))
print('{}의 소인수 : {}'.format(num, primeFactor))

