# 진법 변환하기

uNum = int(input('10진수 입력 : '))

print('10진수 : {} => 2진수 : {}'.format(uNum, bin(uNum)))
print('10진수 : {} => 8진수 : {}'.format(uNum, oct(uNum)))
print('10진수 : {} => 16진수 : {}'.format(uNum, hex(uNum)))

'''
print('10진수 : {} => 2진수 : {}'.format(uNum, format(uNum, "b")))
print('10진수 : {} => 8진수 : {}'.format(uNum, format(uNum, "o")))
print('10진수 : {} => 16진수 : {}'.format(uNum, format(uNum, "x")))
'''

print('2진수(0b10000) => {} (10진수)'.format(int('0b10000', 2)))
print('8진수(0o20) => {} (10진수)'.format(int('0o20', 8)))
print('16진수(0x10) => {} (10진수)'.format(int('0x10', 16)))

print('2진수(0b10000) => {} (8진수)'.format(oct(0b10000)))
print('2진수(0b10000) => {} (10진수)'.format(int(0b10000)))
print('2진수(0b10000) => {} (16진수)'.format(hex(0b10000)))

print('8진수(0o20) => {} (2진수)'.format(bin(0o20)))
print('8진수(0o20) => {} (10진수)'.format(int(0o20)))
print('8진수(0o20) => {} (16진수)'.format(hex(0o20)))