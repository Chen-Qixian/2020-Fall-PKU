#include <bits/stdc++.h>
using namespace std;

int main(void) {
	priority_queue<int, vector<int>, greater<int> > q;
	int t, n, x, sum, a, b;
	scanf("%d", &t);
	while(t --) {
		while(!q.empty()) q.pop();
		scanf("%d", &n);
		while(n --) {
			scanf("%d", &x);
			q.push(x);
		}
		sum = 0;
		while(q.size() > 1) {
			a = q.top();
			q.pop();
			b = q.top();
			q.pop();
			q.push(a+b);
			sum += (a+b);
		}
		printf("%d\n",sum);
	}
	return 0;
}
