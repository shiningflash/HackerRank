#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main() {
    ll n, q, id = 1;
    cin >> n;
    string s[n], z;
    for (int i = 0; i < n; i++) cin >> s[i];
    sort(s, s+n);
    for (cin >> q; q--; ) {
        ll sum = 0;
        cin >> z;
        for (ll i = 0; i < z.length(); i++) {
            if (isupper(z[i])) sum += (z[i] - 'A' + 1);
            else sum += (z[i] - 'a' + 1);
        }
        int pos = lower_bound(s, s+n, z) - s;
        cout << sum * ++pos << endl;
    }
}