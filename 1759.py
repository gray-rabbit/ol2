# https://www.acmicpc.net/problem/1759

# 재귀 함수를 만들거다!
# recu(n, alpha, password, i)
# n 만들어어야 하는 암호의 길이
# alpha 사용할 수 있는 알파벳들 
# password 지금까지 만든 암호
# i 현재 alpha에서 사용할지 결정해야 하는 인덱스

# 1. 정답이 되는 경우 password의길이 == n 
# 2. 정답이 안되는 경우 i>= alpah 길이
# 3. 재귀는?
# 3-1 recu(n, alpha, password + alpha[i], i+1)
# 3-2 recu(n, alpha, password, i+1)
def checker(password):
    mo,ja = 0,0
    for c in password:
        if c in "aeiou":
            mo+=1
        else: ja+=1
    return mo>=1 and ja>=2
    
def recu(n, alpha, password, i):
    if len(password)==n:
        if checker(password):
            print(password)
            return

    if c<=i:
        return 
    
    recu(n, alpha, password+alpha[i], i+1)
    recu(n, alpha, password, i+1)
l,c = map(int, input().split())
s = input().split()
s = sorted(s)
recu(l, s, "", 0)
