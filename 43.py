# 카드 7장을 일렬로 나열하되, 2,4,7번 카드가 서로 이웃하도록 나열하는 모든 경우의 수 구하기

fnum1 = int(input('팩토리얼 숫자 : '))
res1 = 1

for n in range(1, fnum1+1):
    res1 *= n

print(f'res1 : {res1}')

fnum2 = int(input('팩토리얼 숫자 : '))
res2 = 1

for n in range(1, fnum2+1):
    res2 *= n

print(f'res2 : {res2}')
print(f'모든 경우의 수 : {res1*res2}')