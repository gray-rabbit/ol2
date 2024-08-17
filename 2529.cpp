#include <bits/stdc++.h>
using namespace std;
int n = 0;
vector<string> ans;
int checker[10];
char a[100] ; //부등호가 들어있는 배열
bool good(char x, char y, char op){
    if(op=='<'){
        if (x>y) return false;
    }
    if(op=='>'){
        if( x<y) return false;
    }
    return true;
}
void recu(int idx, string nums)
{
    if (idx == n + 1)
    {
        ans.push_back(nums);
        return;
    }
    for (int i = 0; i <= 9; i++)
    {
        if (checker[i])
            continue; // i가 이미 사용되었다!
        if (idx == 0 || good(nums[idx-1], i+'0', a[idx-1])  )
        {
            checker[i] = 1; // i를 사용할꺼야
            recu(idx + 1, nums + to_string(i));
            checker[i] = 0; // i 사용 종료
        }
    }
}