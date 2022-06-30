# 등비수열 : 일반항, n항, Sn 구하기

a1 = 2
r = 3
n = int(input('n 입력 : '))

an = a1 * r**(n-1)
Sn = int(a1 * ((1 - r**n) / (1 - r)))

print('an =a1 * r^(n-1)'.format(a1, r))
print('Sn = a1 * ((1 - r^n) / (1 - r))')
print(f'{n}번째 항 = {an}')
print(f'{n}번째 항 까지의 합 = {Sn}')
