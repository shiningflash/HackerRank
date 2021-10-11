#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x, a;
    deque <int> d;
    for (cin >> n; n--; ) {
        cin >> x;
        if (x == 1) cin >> a, d.push_back(a);
        else if (x == 2) d.pop_front();
        else if (x == 3) cout << d.front() << endl;
    }
}
