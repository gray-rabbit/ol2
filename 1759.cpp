#include <bits/stdc++.h>
using namespace std;
bool checker(string &password)
{
    int ja = 0;
    int mo = 0;
    for (char c : password)
    {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')        {
            mo += 1;
        }
        else
        {
            ja += 1;
        }
    }
    return ja>=2 && mo>=1;
}

void recu(int n, vector<char> &alpha, string password, int i)
{
    if (password.length() == n)
    { // 길이 만족
        if (checker(password))
        {
            cout << password << "\n";
        }
        return;
    }
    if (i >= alpha.size())
        return; // 절대 안되는경우
    recu(n, alpha, password + alpha[i], i + 1);
    recu(n, alpha, password, i);
}

int main()
{
    printf("%d", 10);
}