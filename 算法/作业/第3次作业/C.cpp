#include <bits/stdc++.h>
using namespace std;

int root[1000010];
bool mp[1001][1001];
int t, n, m;

// 并查集找根：路径压缩
int find(int x) {
	if(x == root[x]) return x;
	root[x] = find(root[x]);
	return root[x];
}

// 获取当前点位置：按顺序排列
inline int getloc(int x, int y) {
	return (x - 1) * n + y;
}

int main(void) {
	int a, b, ans, roota, rootb;
	scanf("%d", &t);
	while(t --) {
		scanf("%d%d", &n, &m);
		// 初始化地图，所有开关关闭
		for(int i = 1 ; i <= n ; i++) {
			for(int j = 1 ; j <= n ; j ++) {
				mp[i][j] = false;
			}
		}
		// 初始化并查集
		for(int i = 0 ; i <= n*n+1 ; i ++) {
			root[i] = i;
		}
		// 逐步添加并查集：如果地图上相邻点打开，则合并两个集合
		// 注意边界：x == 1 , x == n 需要将最上层归并到root[0]，最下层归并到root[n*n+1]
		// 若root[0]和root[n*n+1]属于同一个集合，说明上下边界联通
		ans = -1;
		for(int i = 1 ; i <= m ; i ++) {
			scanf("%d%d", &a, &b);
			if(ans != -1) continue;
			mp[a][b] = true;
			// 找到当前点所属的集合
			roota = find(getloc(a, b));
			// 以下逐一判断合并集合
			if(a == 1) {
				rootb = find(0);
				// 注意，必须将已有的点集加入到新的点集当中
				root[rootb] = roota;
			}
			if(a == n) {
				rootb = find(n*n+1);
				root[rootb] = roota;
			}
			if(a > 1 && mp[a-1][b]) {
				rootb = find(getloc(a-1, b));
				root[rootb] = roota;
			}
			if(a < n && mp[a+1][b]) {
				rootb = find(getloc(a+1, b));
				root[rootb] = roota;
			}

			if(b > 1 && mp[a][b-1]) {
				rootb = find(getloc(a, b-1));
				root[rootb] = roota;
			}
			if(b < n && mp[a][b+1]) {
				rootb = find(getloc(a, b+1));
				root[rootb] = roota;
			}
			// 如果因为新加入的点而将上下两端加入同一集合说明联通
			if(find(0) == find(n*n+1)) {
				ans = i;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
