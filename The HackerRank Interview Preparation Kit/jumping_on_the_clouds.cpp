#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, ans(0), a[105];
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) {
        if (i + 2 < n && !a[i + 2]) i++, ans++;
        else if (i + 1 < n && !a[i + 1]) ans++;
    }
    cout << ans << endl;
}