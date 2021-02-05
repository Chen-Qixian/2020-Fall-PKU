#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int n, x;
	int deg[110] = {0};
	vector<int> link[110];
	scanf("%d", &n);
	for(int i = 1; i <= n ; i ++) {
		while(true) {
			scanf("%d", &x);
			if(x == 0) break;
			link[i].push_back(x);
			deg[x] ++;
		}
	}
	queue<int> q;
	for(int i = 1 ; i <= n ; i ++) {
		if(deg[i] == 0) q.push(i);
	}
	while(!q.empty()) {
		x = q.front();
		printf("%d ", x);
		q.pop();
		for(const auto& l: link[x]) {
			deg[l] --;
			if(deg[l] == 0) q.push(l);
		}
	}
	return 0;
}
