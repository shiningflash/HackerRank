#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main() {
    ll n, a(0);
    string s;
    cin >> s >> n;
    ll len = s.length();
    for (int i = 0; i < len; i++) a += (s[i] == 'a');
    ll b = n / len, c = n % len;
    ll ans = a * b;
    for (int i = 0; i < c; i++) ans += (s[i] == 'a');
    cout << ans << endl;
}