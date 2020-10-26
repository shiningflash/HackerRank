#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a[100005];
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    int i = 1, r = 0;
    while(i <= n) {
        int j = a[i-1];
        if (i == j) i++;
        else swap(a[i-1], a[j-1]), r++;
    }
    cout << r << endl;
}