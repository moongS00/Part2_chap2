# 팩토리얼

# 반복문 이용
fac = 1
n = int(input('input number : '))

for i in range(1, n+1):
    fac *= i

print(f'{n}! = {fac}')



# 재귀함수 이용
def facFun(n):
    if n == 1:
        return n

    return n * facFun(n-1)

n = int(input('input number : '))
print(f'{n}! = {facFun(n)}')