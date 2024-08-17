# https://www.acmicpc.net/problem/14889

# 함수이름 recu
# idx 내가 지금 결정해야 하는 사람의 인덱스
# left 스타트팀에 들어간 사람들
# right 링크팀에 들어간 사람들
# recu(idx, left, right) -> 모든 사람들의 팀을 배정하는 함수!

# 1. 정답 idx == n 이 상태에서 판별한다!
# 1-1. 두 팀의 명수가 같은지 판단한다!
# 2. 정답이 아닌 경우 idx > n (필요없다!)
# 3. 재귀 어떻게?
# 3-1, recu(idx+1, left + idx, right)
# 3-1, recu(idx+1, left, right+idx)
# def cal_val(t):
#     val = 0
#     for i in t: #0
#         for j in t:#1
#             val+= l[i][j]
#     return val
# def recu(idx, left, right):
#     if idx==n:
#         if len(left)!=n//2: return 99898999999
#         if len(right)!=n//2: return 99898999999
        
#         # 팀별 점수 계산
#         left_value = cal_val(left)
#         right_value = cal_val(right)
#         diff = left_value-right_value
#         if diff<0 : diff= diff*-1
#         if diff==2:
#             print(left, right)
#         return diff
#     ans = 999999999999
#     ans= min(ans, recu(idx+1, left+[idx], right))
#     ans = min(ans, recu(idx+1, left, right+[idx]))
#     return ans

# n = int(input())
# l = [list(map(int,input().split())) for _ in range(n)]
# print(recu(0, [], []))
x = []

def recu(a):
    if len(a)==10:
        print(a)
        return
    for i in range(10):
        if not i in x:
            x.append(i)
            recu(a+[i])
            x.pop()

recu([])