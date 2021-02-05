#include <bits/stdc++.h>
using namespace std;

const int N = 210;

int n, m, head[N], pre[N], flow[N], cnt;

struct P {
	int a, b, c, next;
} p[N * N];

void addArc(int u, int v, int w) {
	p[cnt].a = u; p[cnt].b = v; p[cnt].c = w; p[cnt].next = head[u];
	head[u] = cnt ++;
	p[cnt].a = v; p[cnt].b = u; p[cnt].c = 0; p[cnt].next = head[v];
	head[v] = cnt ++;
}

void update(int s, int t, int d) {
	int h;
	while(t != s) {
		h = pre[t];
		p[h].c -= d;
		p[h+1].c += d;
		t = p[h].a;
	}
}

int bfs(int s, int t) {
	queue<int> q;
	while(!q.empty()) q.pop();
	memset(pre, -1, sizeof(pre));
	flow[s] = INT_MAX;
	q.push(s);
	while(!q.empty()) {
		int front = q.front();
		q.pop();
		if(front == t) {
			update(s, t, flow[t]);
			return flow[t];
		}
		for(int h = head[front], to; h != -1 ; h = p[h].next) {
			to = p[h].b;
			if(pre[to] == -1 && p[h].c > 0) {
				pre[to] = h;
				flow[to] = min(flow[front], p[h].c);
				q.push(to);
			}
		}
	}
	return 0;
}

int ek(int s, int t) {
	int ans = 0;
	while(true) {
		int d = bfs(s, t);
		if(d <= 0) return ans;
		ans += d;
	}
}

int main(void) {
	int s, c, e;
	while(~scanf("%d%d", &n, &m)) {
		cnt = 0;
		memset(head, -1, sizeof(head));
		memset(flow, 0, sizeof(flow));
		while(n --) {
			scanf("%d%d%d", &s, &c, &e);
			if(s != c) {
				addArc(s, c, e);
			}
		}
		printf("%d\n", ek(1, m));
	}
	return 0;
}
