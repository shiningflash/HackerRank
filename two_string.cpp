#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    string a, b;
    while (n--) {
        cin >> a >> b;
        map<int, int> mp;
        bool f = false;
        for (int i = 0; i < a.length(); i++) mp[a[i]-'a']++;
        for (int i = 0; i < b.length(); i++) {
            if (mp[b[i]-'a']) {
                f = true;
                break;
            }
        }
        cout << (f ? "YES" : "NO") << endl;
    }
}
