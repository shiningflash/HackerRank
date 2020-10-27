#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    string a, b, word;
    cin >> n >> m;
    cin.ignore();
    getline(cin, a);
    getline(cin, b);
    map<string, int> mp;
    stringstream ss(a);
    while (ss >> word) mp[word]++;
    stringstream sss(b);
    bool f = true;
    while (sss >> word) {
        if (mp[word] > 0) mp[word]--;
        else f = false;
    }
    cout << (f ? "Yes\n" : "No\n");
}
