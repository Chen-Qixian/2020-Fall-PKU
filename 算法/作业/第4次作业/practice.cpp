#include <bits/stdc++.h>
using namespace std;

const int INF = 25000;
const int M = 6;

struct Item {
	int k;
	int p;
} item[5];

int ihash[1000];

struct Offer {
	int st;
	int p;
} offer[101];

int base[M] = {1, 6, 36, 216, 1296, 7776};

bool check(int x, int y, int b) {
	for(int i = 0 ; i < b ; i ++) {
		if((x % M + y % M) > item[i].k) return false;
		x /= M;
		y /= M;
	}
	return true;
}

int calculate(int state) {
	int res = 0;
	for(int i = 0 ; state > 0 ; i ++) {
		res += (state % M) * item[i].p;
		state /= M;
	}
	return res;
}

int main(void) {
	// 变量名与题目对应
	int b, c, state = 0, s, n, k;
	scanf("%d", &b);
	for(int i = 0 ; i < b ; i ++) {
		scanf("%d%d%d", &c, &item[i].k, &item[i].p);
		ihash[c] = i;
		state += base[i] * item[i].k;
	}
	scanf("%d", &s);
	for(int i = 0 ; i < s ; i ++) {
		scanf("%d", &n);
		offer[i].st = 0;
		for(int j = 0 ; j < n ; j ++) {
			scanf("%d%d", &c, &k);
			offer[i].st += base[ihash[c]] * k;
		}
		scanf("%d", &offer[i].p);
	}

	int dp[INF];
	dp[0] = 0;
	for(int i = 1 ; i <= state ; i ++) dp[i] = INF;

	for(int i = 0 ; i < s ; i ++) {
		for(int j = 0 ; j <= state ; j ++) {
			if(dp[j] == INF) continue;
			if(j + offer[i].st <= state && check(j, offer[i].st, b)) {
				if(dp[j + offer[i].st] > dp[j] + offer[i].p) {
					dp[j + offer[i].st] = dp[j] + offer[i].p;
				}
			}
		}
	}

	int res = INF;
	for(int i = 0 ; i <= state ; i ++) {
		res = min(res, calculate(state - i) + dp[i]);
	}
	printf("%d\n", res);
	return 0;
}
