#include <bits/stdc++.h>
using namespace std;
const int N = 501;
const int INF = -1;

struct E {
	int next;
	int weight;
};

vector<E> e[N];
int F, P, C, M, cri = 0;
int c[N];
int dis[N];
bool vis[N];

void dijkstra() {
	int newP = 1, size = 0, next, wei, _min;
	dis[newP] = 0;
	vis[newP] = true;
	for(int i = 1 ; i < F ; i ++) {
		size = e[newP].size();
		for(int j = 0 ; j < size ; j ++) {
			next = e[newP][j].next;
			wei = e[newP][j].weight;
			if(vis[next]) continue;
			if(dis[next] == INF || dis[next] > dis[newP] + wei) {
				dis[next] = dis[newP] + wei;
			}
		}
		_min = INT_MAX;
		for(int j = 1 ; j <= F ; j ++) {
			if(vis[j]) continue;
			if(dis[j] == INF) continue;
			if(dis[j] < _min) {
				_min = dis[j];
				newP = j;
			}
		}
		vis[newP] = true;
	}
}

int main(void) {
	while(scanf("%d%d%d%d", &F, &P, &C, &M) != EOF) {
		cri = 0;
		for(int i = 1 ; i <= F ; i ++) {
			e[i].clear();
			dis[i] = INF;
			vis[i] = false;
		}
		int f1, f2, t;
		while(P --) {
			scanf("%d%d%d", &f1, &f2, &t);
			E tmp;
			tmp.next = f2;
			tmp.weight = t;
			e[f1].push_back(tmp);
			tmp.next = f1;
			e[f2].push_back(tmp);
		}
		dijkstra();
		// printf("\n=========\n");
		// for(int i = 1; i <= F ; i ++) {
		// 	printf("%d ", dis[i]);
		// }
		// printf("\n");
		int cow;
		for (int i = 1 ; i <= C ; i ++) {
			scanf("%d", &cow);
			if(dis[cow] != INF && dis[cow] <= M) {
				c[cri ++] = i;
			}
		}
		printf("%d\n", cri);
		for(int i = 0 ; i < cri ; i ++) {
			printf("%d\n", c[i]);
		}
	}
	return 0;
}
