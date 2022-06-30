# 등차수열 : 일반항, n항, Sn 구하기

a1 = 4
d = 6
n = int(input('n 입력 : '))

an = a1 + (n-1)*d
Sn = int(n*(a1 + an) / 2)

print('an = {} + (n-1)*{}'.format(a1, d))
print('Sn = n*(a1 + an) / 2')
print(f'{n}번째 항 = {an}')
print(f'{n}번째 항 까지의 합 = {Sn}')

