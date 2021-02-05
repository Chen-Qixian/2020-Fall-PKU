#include <bits/stdc++.h>
using namespace std;

// 先打印归并排序模板
int cnt = 0;

void merge(vector<int>& a, int l, int r) {
	if(l >= r) return;
	int m = l + (r - l) / 2, i = l, j = m + 1, p = i, k = 0;
	vector<int> tmp(r - l + 1);
	while(i <= m && j <= r) {
		if(a[i] > a[j]) {
			// 关键：每次移动j的时候，说明已经有逆序产生，判断该移动所贡献的重要逆序对数，移动指针p，找到第一个满足2倍关系的数
			while(p <= m && a[p] <= 2 * a[j]) p ++;
			// 注意：当p已经移除前半段范围时，说明不可能贡献更多的重要逆序对
			if(p < m + 1) cnt += m + 1 - p;
			tmp[k ++] = a[j ++];
		}
		else {
			tmp[k ++] = a[i ++];
		}
	}
	// 关键： 当任意一段数字用尽，则不可能贡献更多的重要逆序对
	while(i <= m) tmp[k ++] = a[i ++];
	while(j <= r) tmp[k ++] = a[j ++];
	copy(tmp.begin(), tmp.end(), a.begin() + l);
}

void mergeSort(vector<int>& a, int left, int right) {
	if(left >= right) return;
	int mid = left + (right - left) / 2;
	mergeSort(a, left, mid);
	mergeSort(a, mid + 1 , right);
	merge(a, left, right);
}

int main(void) {
	int n;
	while(scanf("%d", &n) != EOF) {
		if(n == 0) break;
		vector<int> a(n);
		for(int i = 0 ; i < n ; i ++) {
			scanf("%d", &a[i]);
		}
		cnt = 0;
		mergeSort(a, 0, n-1);
		// for (const auto& v:a) cout << v << " ";
		printf("%d\n", cnt);
	}
	return 0;
}
