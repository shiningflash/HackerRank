#include <bits/stdc++.h>
using namespace std;
#define ll long long int

ll arr[10000005];

int main() {
    ll n, m, a, b, x;
    cin >> n >> m;
    for (ll i = 0; i < m; i++) {
        cin >> a >> b >> x;
        arr[a-1] += x;
        if (b < n) arr[b] -= x;
    }
    ll r = 0, mx = 0;
    for (ll i = 0; i < n; i++) {
        r += arr[i];
        if (r > mx) mx = r;
    }
    cout << mx << endl;
}