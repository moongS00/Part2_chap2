# 피보나치 수열 : an = an-2 + an-1

a1 = 1
a2 = 1
an = 0
sig = 0
n = 5

for i in range(1, n+1):
    if i < 3:
        print(f'{i}항 : {a1}')
        sig += a1
        print(f'{i}항 까지 합 : {sig}')
        continue

    an = a1 + a2
    a1 = a2
    a2 = an
    sig += an
    print(f'{i}항 : {an}')
    print(f'{i}항 까지 합 : {sig}')