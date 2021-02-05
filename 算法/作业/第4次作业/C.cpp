#include <bits/stdc++.h>
using namespace std;

unordered_map<char, unordered_map<char, int> > mp;

void init_map() {
	mp['A']['A'] =  5; mp['A']['C'] = -1; mp['A']['G'] = -2; mp['A']['T'] = -1; mp['A']['-'] = -3;
	mp['C']['A'] = -1; mp['C']['C'] =  5; mp['C']['G'] = -3; mp['C']['T'] = -2; mp['C']['-'] = -4;
	mp['G']['A'] = -2; mp['G']['C'] = -3; mp['G']['G'] =  5; mp['G']['T'] = -2; mp['G']['-'] = -2;
	mp['T']['A'] = -1; mp['T']['C'] = -2; mp['T']['G'] = -2; mp['T']['T'] =  5; mp['T']['-'] = -1;
	mp['-']['A'] = -3; mp['-']['C'] = -4; mp['-']['G'] = -2; mp['-']['T'] = -1;
}

int main(void) {
	init_map();
	int T, m, n;
	char s1[101], s2[101];
	int dp[110][110];
	scanf("%d", &T);
	while(T -- > 0) {
		scanf("%d%s%d%s", &m, s1, &n, s2);
		// printf("\n%s\n%s", s1, s2);
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 0;
		for(int i = 1 ; i <= m ; i ++) {
			dp[i][0] = dp[i-1][0] + mp[s1[i-1]]['-'];
		}
		for(int j = 1 ; j <= n ; j ++) {
			dp[0][j] = dp[0][j-1] + mp['-'][s2[j-1]];
		}
		for(int i = 1 ; i <= m ; i ++) {
			for(int j = 1 ; j <= n ; j ++) {
				dp[i][j] = max(dp[i-1][j-1] + mp[s1[i-1]][s2[j-1]],
				           max(dp[i][j-1] + mp['-'][s2[j-1]], dp[i-1][j] + mp[s1[i-1]]['-']));
			}
		}
		// for(int i = 0 ; i <= m ; i ++) {
		// 	for(int j = 0 ; j <= n ; j ++) {
		// 		printf("%d ", dp[i][j]);
		// 	}
		// 	printf("\n");
		// }
		printf("%d\n", dp[m][n]);
	}
	return 0;
}
