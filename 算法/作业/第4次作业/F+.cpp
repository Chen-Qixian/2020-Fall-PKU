#include <bits/stdc++.h>
using namespace std;

unordered_map<int, int> mp;
map<vector<int>, int> result;
int b;

vector<int> helper(const vector<int>& sp, vector<int>& need) {
	int size = need.size();
	vector<int> rem(size);
	for(int i = 0 ; i < size ; i ++) {
		if(sp[i] > need[i]) return {};
		rem[i] = need[i] - sp[i];
	}
	return rem;
}

int dfs(vector<int>& price, vector<int>& need, vector<vector<int> >& special) {
	if(result.count(need)) return result[need];
	int res = inner_product(price.begin(), price.end(), need.begin(), 0);
	for(const auto& sp: special) {
		auto rem = helper(sp, need);
		if(rem.empty()) continue;
		res = min(res, sp[b] + dfs(price, rem, special));
	}
	result[need] = res;
	return res;
}

int main(void) {
	int c, k , p, s, n, cnt = 0, ans;
	scanf("%d", &b);
	vector<int> price(b);
	vector<int> need(b);
	for(int i = 0 ; i < b ; i ++) {
		scanf("%d%d%d", &c, &k, &p);
		mp[c] = cnt;
		need[cnt] = k;
		price[cnt ++] = p;
	}
	scanf("%d",&s);
	vector<vector<int> > special(s, vector<int>(b+1, 0));
	cnt = 0;
	while(s -- > 0) {
		scanf("%d", &n);
		for(int i = 0 ; i < n ; i ++) {
			scanf("%d%d", &c, &k);
			special[cnt][mp[c]] = k;
		}
		scanf("%d", &p);
		special[cnt ++][b] = p;
	}
	ans = dfs(price, need, special);
	printf("%d\n", ans);
	return 0;
}
