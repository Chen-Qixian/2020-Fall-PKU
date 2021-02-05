#include <bits/stdc++.h>
using namespace std;

int dp[101][25000];

int main(void) {
	int n, sum = 0, m, w;
	int a[101];
	scanf("%d", &n);
	for(int i = 0 ; i < n ; i ++) {
		scanf("%d", &a[i]);
		sum += a[i];
	}
	// 转换成0-1背包问题：限制背包个数为：人数的一半（向上取整），背包容量为：总体重一半（向上取整）
	w = (sum + 1) / 2;
    m = (n + 1) / 2;
    memset(dp, 0, sizeof(dp));
    for(int k = 0 ; k < n ; k ++) {
    	// 0-1背包：每个元素只能选择 取 或者 不取。因此从大到小遍历。
    	for(int i = m ; i >= 1 ; i --) {
    		for(int j = w ; j >= a[k] ; j --) {
    			dp[i][j] = max(dp[i][j], dp[i-1][j-a[k]] + a[k]);
    		}
    	}
    }
    printf("%d %d", min(dp[m][w], sum - dp[m][w]), max(dp[m][w], sum - dp[m][w]));
	return 0;
}
