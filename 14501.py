# https://www.acmicpc.net/problem/14501

# 함수 recu ( day, sum) 
# day는 몇번 째 날이냐, sum 지금까지 얼마의 수익을 얻었는가?

# 1. 정답 day==n+1
# 2. 불가능 day > n+1
# 3. 재귀
# 3-1. 상담한다 go(day + t[day], sum + v[day])
# 3-2. 상담안한다 go(day+1, sum)

def recu(day, sum):
    if day==n:
        return sum
    if day>n:
        return 0
    ans = 0
    ans = max(ans, recu(day+t[day], sum+v[day]))
    ans = max(ans, recu(day+1, sum))
    return ans
n = int(input())
t, v = [], []
for _ in range(n):
    tt, vv = map(int, input().split())
    t.append(tt)
    v.append(vv)
print(recu(0,0))
