#include <bits/stdc++.h>
using namespace std;

// # 함수이름 recu
// # idx 내가 지금 결정해야 하는 사람의 인덱스
// # left 스타트팀에 들어간 사람들
// # right 링크팀에 들어간 사람들
// # recu(idx, left, right) -> 모든 사람들의 팀을 배정하는 함수!

// # 1. 정답 idx == n 이 상태에서 판별한다!
// # 1-1. 두 팀의 명수가 같은지 판단한다!
// # 2. 정답이 아닌 경우 idx > n (필요없다!)
// # 3. 재귀 어떻게?
// # 3-1, recu(idx+1, left + idx, right)
// # 3-1, recu(idx+1, left, right+idx)
int n = 0;
int value[100][100] ;
int recu(int idx, vector<int> &left, vector<int> &right){
    if(idx==n){ //이제 모든 팀이 나누어졌다.
        if(left.size()!=n/2) return -1;
        if(right.size()!=n/2) return -1;
        int left_v = 0; //스타트팀 점수
        int right_v = 0; //링크팀 점수
        for(int i=0;i<n/2;i++){
            for(int j=0;j<n/2;j++){
                if(i==j) continue;
                left_v += value[left[i]][left[j]] ;
                right_v+= value[right[i]][right[j]];
            }
        }
        int diff = left_v-right_v;
        if(diff<0) diff*=-1;
        return diff;
    }
    int ans =-1;
    left.push_back(idx); //스타팀에 넣었다. 
    int lv = recu(idx+1, left, right);
    if(ans==-1 || (lv!=-1 && ans>lv)){
        ans = lv;
    }
    left.pop_back();
    right.push_back(idx); //링크에 넣었다. 
    int rv = recu(idx+1, left, right);
    if(ans==-1 || (rv!=-1 && ans>rv)){
        ans = rv;
    }
    right.pop_back();
    return ans;
}