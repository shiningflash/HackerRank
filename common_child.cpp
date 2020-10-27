#include <bits/stdc++.h>
using namespace std;

int dp[5002][5002];

int LCS(string a, string b, int m, int n) {
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0) dp[i][j] = 0;
            else if (a[i-1] == b[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
            else dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }
    return dp[m][n];
}

int main() {
    string a, b;
    cin >> a >> b;
    cout << LCS(a, b, a.length(), b.length()) << endl;
}
