#include <bits/stdc++.h>
using namespace std;


int T, N;
int a[50001];
int dpl[50001];
int dpr[50001];

void left() {
	dpl[0] = a[0];
	for(int i = 1 ; i < N ; i ++) {
		dpl[i] = max(a[i], a[i] + dpl[i-1]);
	}
	for(int i = 1 ; i < N ; i ++) {
		dpl[i] = max(dpl[i], dpl[i-1]);
	}
}

void right() {
	dpr[N-1] = a[N-1];
	for(int i = N - 2 ; i >= 0 ; i --) {
		dpr[i] = max(a[i], a[i] + dpr[i+1]);
	}
	for(int i = N - 2 ; i >= 0 ; i --) {
		dpr[i] = max(dpr[i], dpr[i+1]);
	}
}

int getAns() {
	int res = INT_MIN;
	for(int i = 0 ; i < N - 1 ; i ++) {
		res = max(res, dpl[i] + dpr[i+1]);
	}
	return res;
}

int main(void) {
	scanf("%d", &T);
	while(T--) {
		scanf("%d", &N);
		for(int i = 0 ; i < N ; i ++) {
			scanf("%d", &a[i]);
		}
		left();
		right();
		int ans = getAns();
		printf("%d\n", ans);
	}
	return 0;
}
