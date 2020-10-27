#include <bits/stdc++.h>
using namespace std;
#define ll long long int

ll get_sum(ll n, ll x) {
    ll d = n / x;
    d = (d * (d + 1)) / 2;
    return x * d;
}

int main() {
    ll t, n, x;
    for (cin >> t; t--; ) {
        cin >> n;
        n--;
        ll sum = get_sum(n, 3);
        sum += get_sum(n, 5);
        sum -= get_sum(n, 15);
        cout << sum << endl;
    }
}