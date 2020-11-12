#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    string s;
    for (cin >> n; n--; ) {
        cin >> s;
        int x = s.length(), cnt = 0;
        map <int, int> mp;
        for (int i = 0; i < x; i++) {
            if (mp[s[i]-'A'] == 0) cnt++, mp[s[i]-'A']++; 
        }
        cout << cnt << endl;
    }
}