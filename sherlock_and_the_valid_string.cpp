#include <bits/stdc++.h>
using namespace std;

int main() {
    string str;
    map<int, int> m;
    cin >> str;
    int len = str.length();
    for (int i = 0; i < len; i++) m[str[i]-'a']++;
    set<int> s;
    for (int i = 0; i < 26; i++) if (m[i] != 0) s.insert(m[i]);
    if (s.size() > 2) cout << "NO\n";
    else if (s.size() == 1) cout << "YES\n";
    else {
        vector<int> v;
        set<int>::iterator it;
        for (it = s.begin(); it != s.end(); it++) v.push_back(*it);
        map<int, int> m2;
        for (int i = 0; i < 26; i++) m2[m[i]]++;
        // cout << v[0] << " " << m2[v[0]] << " " << v[1] << " " << m2[v[1]] << endl;
        if (m2[v[0]] == 1 || m2[v[1]] == 1) {
            if (abs(v[0] - v[1]) <= 1 || (v[0] == 1 && m2[v[0]] == 1) || (v[1] == 1 && m2[v[1]] == 1)) cout << "YES\n";
            else cout << "NO\n";
        }
        else cout << "NO\n";
    }
}
