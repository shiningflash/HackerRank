#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x, ans(0);
    map <int, int> mp;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> x, mp[x]++;
    for (int i = 1; i <= 100; i++) ans += (mp[i] >> 1);
    cout << ans << endl;
}
