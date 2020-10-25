#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, d, a[100005];
    cin >> n >> d;
    d = d % n;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = d, j = 0; j < n; i = (i + 1) % n, j++) cout << a[i] << " ";
    cout << endl;
}