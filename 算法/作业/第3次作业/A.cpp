#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int judge[1001][1001] = {{-1}};
int graph[1001][1001] = {{0}};
int vert[1001] = {-1};
bool vis[1001] = {false};
int seq[100001][3];

void bfs(const int& n) {
	queue<int> q;
	q.push(0);
	vis[0] = true;
	vert[0] = 0;
	while(!q.empty()) {
		int now = q.front();
		q.pop();
		for(int i = 0 ; i < n ; i ++) {
			if(!vis[i] && graph[now][i] == 1) {
				if(judge[now][i] == 0) {
					vert[i] = vert[now];
				}
				else if(judge[now][i] == 1) {
					vert[i] = (vert[now]==0) ? 1 : 0;
				}
				vis[i] = true;
				q.push(i);
			}
		}
	}
}

bool check(const int& n, const int& m) {
	int a, b, f;
	for(int i = 0 ; i < n ; i ++) {
		if(vert[i] == -1) {
			return false;
		}
	}
	for(int i = 0 ; i < m ; i ++) {
		a = seq[i][0];
		b = seq[i][1];
		f = seq[i][2];
		if(f == 0) {
			if(vert[a] != vert[b]) {
				return false;
			}
		}
		else if(f == 1) {
			if(vert[a] == vert[b]) {
				return false;
			}
		}
	}

	return true;
}

int main(void) {
	int n, m;
	while(scanf("%d%d", &n, &m) != EOF) {
		int a, b, flag;
		for(int i = 0 ; i < n ; i ++) {
			vert[i] = -1;
			vis[i] = false;
		}
		for(int i = 0 ; i < m ; i ++) {
			scanf("%d%d%d", &a, &b, &flag);
			judge[a][b] = flag;
			judge[b][a] = flag;
			graph[a][b] = 1;
			graph[b][a] = 1;
			seq[i][0] = a;
			seq[i][1] = b;
			seq[i][2] = flag;
		}

		bfs(n);

		if(check(n, m)) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}



	return 0;
}
