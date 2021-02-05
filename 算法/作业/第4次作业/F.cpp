#include <bits/stdc++.h>
using namespace std;
// dp的最大价值，999元/件 * 25件
const int INF = 25000;
// 建立从编号到物品顺序ID的映射
int _hash[1000];
// 存储每种物品数量、价值：种类不超过5
struct Item {
	int cnt;
	int p;
} item[5];
// 存储打折组合：【技巧】用6的幂次记录对应种类物品数量
// 对6求余数刚好0-5表示该种物品能出现的次数
// 最多100个offer
struct Offer {
	int st; // 该offer中所含各种物品数量的状态码
	int price;
	Offer(): st(0), price(0) {}
} offer[101];
// 下标i对应第i类物品状态码的基数值
int base[6] = {1, 6, 36, 216, 1296, 7776};

// 检查两种状态下每种物品之和是否超出限定值
bool check(int x, int y, int n) {
	for(int i = 0 ; i < n ; i ++) {
		if((x % 6 + y % 6) > item[i].cnt) return false;
		x /= 6;
		y /= 6;
	}
	return true;
}

// 计算单独购买每种商品的花费
int calculate(int state) {
	int cost = 0;
	for(int i = 0 ; state > 0 ; i ++) {
		cost += (state % 6) * item[i].p;
		state /= 6;
	}
	return cost;
}

int main(void) {
	// 全局变量:
	// state表示目标组合中各种类商品数量的状态值
	// code为物品种类代码
	// num为offer中每种物品个数
	// p为offer中含有物品种类数
	int n, m, state = 0, code, num, p;
	int dp[INF];
	scanf("%d", &n);
	for(int i = 0 ; i < n ; i ++) {
		scanf("%d%d%d", &code, &item[i].cnt, &item[i].p);
		_hash[code] = i;
		state += base[i] * item[i].cnt;
	}
	scanf("%d", &m);
	for(int i = 0 ; i < m ; i ++) {
		scanf("%d", &p);
		for(int j = 0 ; j < p ; j ++) {
			scanf("%d%d", &code, &num);
			offer[i].st += base[_hash[code]] * num;
		}
		scanf("%d", &offer[i].price);
	}
	// 初始化dp，dp[i]表示物品组合为了达到组合状态为i时的最小花费
	dp[0] = 0;
	for(int i = 1 ; i <= state ; i ++) dp[i] = INF;
	// 遍历各种offer，尝试将该offer加入或不加入的最低花费
	// 完全背包问题从小到大遍历
	for(int i = 0 ; i < m ; i ++) {
		for(int j = 0; j <= state; j ++) {
			if(dp[j] == INF) continue;
			if(j + offer[i].st && check(j, offer[i].st, n)) {
				if(dp[j + offer[i].st] > dp[j] + offer[i].price) {
					dp[j + offer[i].st] = dp[j] + offer[i].price;
				}
			}
		}
	}
	int ans = INF;
	for(int i = 0 ; i <= state ; i ++) {
		// 前i状态使用offer后面的状态均单独购买，计算最小值
		ans = min(calculate(state - i) + dp[i], ans);
	}
	printf("%d\n", ans);
	return 0;
}
