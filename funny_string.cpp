#include <bits/stdc++.h>
using namespace std;

bool isFunny(string s, string r) {
    for (int i = 0; i < s.length()-1; i++) {
        if (abs(s[i]-s[i+1]) != abs(r[i]-r[i+1])) return false;
    }
    return true;
}

int main() {
    int n;
    for (cin >> n; n--; ) {
        string s, r = "";
        cin >> s;
        for (int i = s.length()-1; i >= 0; i--) r.push_back(s[i]);
        cout << (isFunny(s, r) ? "Funny" : "Not Funny") << endl;
        
    }
}