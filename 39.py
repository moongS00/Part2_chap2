# 계차수열

an = 2
n = 30
bn = 3
d = 3

for i in range(1, n+1):
    if i == 1:
        print(f'an{i}항 : {an}')
        print(f'bn{i}항 : {bn}')
        continue

    an += bn
    bn += d
    print(f'an{i}항 : {an}')
    print(f'bn{i}항 : {bn}')