#include <bits/stdc++.h>
using namespace std;
int n =0;
int t[200];
int v[200];
int ans = 0 ;
void recu(int day, int sum){
    if(day == n+1){
        if(ans<sum) ans = sum;
        return;
    }
    if(day>n+1) return ; //불가능

    recu(day+t[day], sum+v[day]); //상담한다.
    recu(day+1, sum); //상담 안한다.
}