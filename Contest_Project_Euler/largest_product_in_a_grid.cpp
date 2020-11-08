#include <bits/stdc++.h>
using namespace std;

int a[25][25], mx = 0;

int main() {
    for (int i = 0; i < 20; i++) for (int j = 0; j < 20; j++) cin >> a[i][j];
    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 20; j++) {
            int right = 0, down = 0, diag1 = 0, diag2 = 0;
            right = a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3];
            down = a[i][j] * a[i+1][j] * a[i+2][j] * a[i+3][j];
            diag1 = a[i][j] * a[i+1][j+1] * a[i+2][j+2] * a[i+3][j+3];
            if (i < 20 - 3 && j > 2) diag2 = a[i][j] * a[i+1][j-1] * a[i+2][j-2] * a[i+3][j-3];
            
            if (right > mx) mx = right;
            if (down > mx) mx = down;
            if (diag1 > mx) mx = diag1;
            if (diag2 > mx) mx = diag2;
        }
    }
    cout << mx << endl;
}