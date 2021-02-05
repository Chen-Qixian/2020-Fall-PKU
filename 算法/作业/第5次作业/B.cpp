#include <bits/stdc++.h>
using namespace std;

// 使用bellman_ford判断是否存在正环
// 权重的更新：dis[b] < (dis[a] - c) * r 时更新

const int N = 300;

struct P {
	int a, b;
	double r, c;
} p[N];

int n, m, s, cnt;
double v, dis[N];

bool bellman_ford() {
	// 距离向量dis表示经过松弛后，到达该点的最大现金值，初始化为0，到源点的值为V
	memset(dis, 0, sizeof(dis));
	dis[s] = v;
	bool flag;
	int a, b;
	double r, c;
	// 进行 n-1 次松弛（即最长路径最多n-1条边），若松弛后仍能继续松弛，则存在正环
	for(int i = 0 ; i < n - 1 ; i ++) {
		// 若遍历完cnt对边后无法继续松弛，则break
		flag = true;
		// 遍历cnt对有向边
		for(int j = 0 ; j < cnt ; j ++) {
			a = p[j].a; b = p[j].b; r = p[j].r; c = p[j].c;
			if(dis[b] < (dis[a] - c) * r) {
				dis[b] = (dis[a] - c) * r;
				flag = false;
			}
		}
		// 若遍历完cnt对边后无法继续松弛，则break
		if(flag) break;
	}

	for(int j = 0 ; j < cnt ; j ++) {
		a = p[j].a; b = p[j].b; r = p[j].r; c = p[j].c;
		if(dis[b] < (dis[a] - c) * r) {
			return true;
		}
	}
	return false;
}

int main(void) {
	int a, b;
	double rab, cab, rba, cba;
	while(~scanf("%d%d%d%lf", &n, &m, &s, &v)) {
		cnt = 0;
		for(int i = 0 ; i < m ; i ++) {
			scanf("%d%d%lf%lf%lf%lf", &a, &b, &rab, &cab, &rba, &cba);
			// 存储cnt = m * 2 对有向带权边
			p[cnt].a = a; p[cnt].b = b; p[cnt].r = rab; p[cnt ++].c = cab;
			p[cnt].a = b; p[cnt].b = a; p[cnt].r = rba; p[cnt ++].c = cba;
		}
		if(bellman_ford()) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
