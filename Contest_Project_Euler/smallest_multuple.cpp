#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    for (cin >> n; n--; ) {
        cin >> x;
        int mul = 1;
        // find lcm
        for (int i = 2; i <= x; i++) mul = (mul * (i / __gcd(mul, i)));
        cout << mul << endl;
    }
}
