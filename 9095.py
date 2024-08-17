# https://www.acmicpc.net/problem/9095

# 함수를 만들거다.
# 숫자 count개 로 합 sum을 만든다!
# 만들고 싶은 수를 goal
# 1. 정답 sum == goal
# 2. 불가능 sum > goal
# 3. 재귀를 어떻게?
# sum  + 1, sum+2, sum+3

def recu(sum):
    if sum==goal: return 1
    if sum>goal: return 0
    ans = 0
    ans += recu(sum+1)
    ans += recu(sum+2)
    ans += recu(sum+3)
    return ans

n = int(input())
for _ in range(n):
    goal = int(input())
    print(recu(0))