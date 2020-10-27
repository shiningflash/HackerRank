#include <bits/stdc++.h>
using namespace std;
 
int main() {
    string a, b;
    map<int, int> m1, m2;
    cin >> a >> b;
    for (int i = 0; i < a.length(); i++) m1[a[i]-'a']++;
    for (int i = 0; i < b.length(); i++) m2[b[i]-'a']++;
    int ans = 0;
    for (int i = 0; i < 26; i++) ans += abs(m1[i] - m2[i]);
    cout << ans << endl;
}
