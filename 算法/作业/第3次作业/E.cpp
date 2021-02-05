#include <bits/stdc++.h>
using namespace std;

struct Dur{
	double l;
	double r;
	bool operator< (const Dur& D) const {
		return l < D.l;
	}
};
vector<Dur> v;


int main(void) {
	int n;
	double a, b, d;
	bool flag;
	int t = 1;
	while(true) {
		scanf("%d%lf", &n, &d);
		if(n == 0 && d == 0) break;
		flag = false;
		v.clear();
		while(n --) {
			scanf("%lf%lf", &a, &b);
			if(b > d) {
				flag = true;
				continue;
			}
			Dur dur;
			dur.l = a * 1.0 - sqrt(d*d - b*b);
			dur.r = a * 1.0 + sqrt(d*d - b*b);
			v.push_back(dur);
		}
		printf("Case %d: ", t);
		if(flag) {
			printf("-1\n");
			t ++;
			continue;
		}
		sort(v.begin(), v.end());
		Dur tmp = v[0];
		int size = v.size();
		int cnt = 1;
		for(int i = 1 ; i < size ; i ++) {
			if(v[i].l > tmp.r) {
				cnt ++;
				tmp = v[i];
			}
			else if(v[i].r < tmp.r) {
				tmp = v[i];
			}
		}
		printf("%d\n", cnt);
		t ++;
	}
	return 0;
}
