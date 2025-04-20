#입력 Input
a = int(input())
b = int(input())

#처리 process
print(a * (b % 10))
print(a * (b // 10 % 10))
print(a * (b//100))
print(a * b)