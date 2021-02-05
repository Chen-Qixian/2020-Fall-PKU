#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int n, t;
	vector<int> a(110);
	scanf("%d", &n);
	for(int i = 0 ; i < n ; i ++) {
		scanf("%d", &a[i]);
	}
	vector<vector<int> > dp(110, vector<int>(110, 0));
	for(int i = 0; i < n - 2 ; i ++) {
		dp[i][i+2] = a[i] * a[i+1] * a[i+2];
	}
	for(int len = 4 ; len <= n ; len ++) {
		for(int i = 0 ; i + len <= n ; i ++) {
			t = i + len - 1;
			dp[i][t] = INT_MAX;
			for(int k = i + 1 ; k < t ; k ++) {
				dp[i][t] = min(dp[i][t], dp[i][k] + dp[k][t] + a[i] * a[k] * a[t]);
			}
		}
	}
	printf("%d", dp[0][n-1]);
	return 0;
}
