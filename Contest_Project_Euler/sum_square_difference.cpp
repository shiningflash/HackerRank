#include <bits/stdc++.h>
using namespace std;
#define ll long long int
 
ll arr[10005];
 
void init() {
    for (int i = 0; i < 10002; i++) arr[i] = arr[i-1] + (i*i);
}
 
void solve() {
    ll n; cin >> n;
    ll x = (n * (n+1)) / 2;
    cout << (x * x) - arr[n] << endl;
}
 
int main() {
    int n;
    init();
    for (cin >> n; n--; ) solve();
}
