#include <bits/stdc++.h>
using namespace std;
#define ll long long int
 
void solve() {
    ll n, k, ans = 0LL;
    string s;
    cin >> n >> k >> s;
    for (int i = 0; i + k < n; i++) {
        ll prod = 1LL;
        bool f = 1;
        for (int j = 0; j < k; j++) {
            prod *= (s[i+j] - '0');
            if (s[i+j] == '0') {
                f = 0;
                break;
            }
        }
        if (f) if (prod > ans) ans = prod;
    }
    cout << ans << endl;
}
 
int main() {
    ll t;
    for (cin >> t; t--; ) solve();
}
