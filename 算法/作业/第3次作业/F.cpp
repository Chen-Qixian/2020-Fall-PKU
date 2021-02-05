#include <bits/stdc++.h>
using namespace std;

struct E {
	int a;
	int b;
	int w;
	bool operator< (const E& e) const {
		return w < e.w;
	}
};

int g[110][110];
int v[110];

int find(int x) {
	if(v[x] == -1) return x;
	v[x] = find(v[x]);
	return v[x];
}

int main(void) {
	int n, roota, rootb, size, ans;
	while(scanf("%d", &n) != EOF) {
		vector<E> edge;
		for(int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < n ; j ++) {
				scanf("%d", &g[i][j]);
			}
			v[i] = -1;
		}
		for(int i = 0 ; i < n - 1 ; i ++) {
			for(int j = i + 1; j < n ; j ++) {
				E e;
				e.a = i;
				e.b = j;
				e.w = g[i][j];
				edge.push_back(e);
			}
		}
		sort(edge.begin(), edge.end());
		size = edge.size();
		ans = 0;
		for(int i = 0 ; i < size ; i ++) {
			roota = find(edge[i].a);
			rootb = find(edge[i].b);
			if(roota != rootb) {
				v[roota] = rootb;
				ans += edge[i].w;
			}
		}
		printf("%d\n", ans);

	}
	return 0;
}
