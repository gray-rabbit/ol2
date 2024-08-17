n = int(input())
l = input().split()
checker = [0] * 10 #사용했는지 확인
min_v = "999"
max_v = "000"
def good(x, y, op):
    if op==">" and x > y: return True
    if op=="<" and x < y: return True
    return False
def recu(idx, nums, min_v, max_v):
    if idx==n+1:
        min_v = min(min_v, nums)
        max_v = max(max_v, nums)
        return min_v, max_v
    for i in range(10):
        if checker[i]: continue #이미 사용되었다면 그냥 지나간다
        if idx==0 or (good(int(nums[-1]), i, l[idx-1] )):
            checker[i] = 1
            min_v, max_v = recu(idx+1, nums+str(i), min_v, max_v)
            checker[i] = 0
    return min_v, max_v
min_v, max_v = recu(0, "",min_v, max_v)
print(max_v, min_v ,sep="\n" )
    
