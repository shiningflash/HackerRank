#include <bits/stdc++.h>
using namespace std;

int t, n, a[100005];

void solve() {
    cin >> n;
    int ans = 0;
    for (int i = 1; i <= n; i++) cin >> a[i];
    for (int i = n; i >= 1; i--) {
        if (a[i] != i) {
            if (a[i-1] == i) {
                swap(a[i], a[i-1]);
                ans++;
            }
            else if (a[i-2] == i) {
                a[i-2] = a[i-1];
                a[i-1] = a[i];
                a[i] = i;
                ans += 2;
            }
            else {
                cout << "Too chaotic\n";
                return;
            }
        }
    }
    cout << ans << endl;
}

int main() {
    for (cin >> t; t--; ) solve();
}