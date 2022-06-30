# 첫째날 쌀 두톨을 받고 둘째날부터는 하루 전의 2배에 해당하는 쌀을 받는다고 할때
# 30일째 되는 날 받게 되는 쌀의 개수를 수열과 시그마로 출력해라

a1 = 2
r = 2
an = a1
Sig = a1

for i in range(1, 31):
    if i == 1:
        print(f'{i}일에 받은 쌀의 개수 : {an}')
        print(f'{i}일 까지 받은 쌀의 개수 : {Sig}')
        continue

    an *= r
    Sig += an
    print(f'{i}일에 받은 쌀의 개수 : {an}')
    print(f'{i}일 까지 받은 쌀의 개수 : {Sig}')