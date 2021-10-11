#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    string s;
    for (cin >> n; n--; ) {
        int dup = 0;
        cin >> s;
        for (int i = 0; i < s.length()-1; i++) if (s[i] == s[i+1]) dup++;
        cout << dup << endl;
    }
}
