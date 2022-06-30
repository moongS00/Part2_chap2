# 군수열

sum = 0
n = 1

flag = True
while flag:
    for i in range(1, n+1):
        print(f'{i}/{n-i+1}\t', end='')
        sum += (i / (n - i + 1))

    if sum > 100:
        print(f'합이 최초로 100을 초화하는 항 : {n}항, {i}/{n-i+1}')
        flag = False
        break

    print()
    n += 1