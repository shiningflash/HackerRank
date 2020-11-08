#include <bits/stdc++.h>
#include <fstream> 
using namespace std;

vector <string> getLog(string fileName) {
    ofstream f1;
    f1.open(fileName);
    vector <string> v1;
    string s;
    while (f1) {
        getline(cin, s);
        if (s == "-1") break;
        v1.push_back(s);
    }
    f1.close();
}

int main() {
    vector <string> v1 =  getLog("f1.txt");
    vector <string> v2 =  getLog("f2.txt");
    map<string, int> m;
    for (int i = 0; i < v2.size(); i++) {
        m[v2[i]]++;
    }
    int cnt = 0;
    for (int i = 0; i < v1.size(); i++) {
        if (m[v1[i]] > 0) {
            cout << v1[i] << endl;
            m[v1[i]]--;
            cnt++;
        }
    }
    cout << cnt << endl;
}