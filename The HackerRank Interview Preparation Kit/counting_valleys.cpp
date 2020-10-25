#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x(0), ans(0);
    string s;
    cin >> n >> s;
    for (int i = 0; i < n; i++) {
        s[i] == 'U' ? x++ : x--;
        if (!x && s[i] == 'U') ans++;
    }
    cout << ans << endl;
}