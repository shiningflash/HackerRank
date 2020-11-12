#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x(0); cin >> n;
    string s; cin >> s;
    for (int i = 0; i < s.length()-2; i++) {
        if (s[i] == '0' && s[i+1] == '1' && s[i+2] == '0') {
            s[i+2] == '1';
            x++; i += 2;
        }
    }
    cout << x << endl;
}