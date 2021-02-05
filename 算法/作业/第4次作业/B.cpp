#include <bits/stdc++.h>
using namespace std;

inline double getDist(int x1, int y1, int x2, int y2) {
	return (double) sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main(void) {
	int T, N, sta[1001][2], age[1001][2];
	double dist;
	scanf("%d", &T);
	while(T-- > 0) {
		scanf("%d", &N);
		for(int i = 0 ; i < N ; i ++) {
			scanf("%d%d", &sta[i][0], &sta[i][1]);
		}
		double res = (double) INT_MAX;
		for(int i = 0 ; i < N ; i ++) {
			scanf("%d%d", &age[i][0], &age[i][1]);
			for(int j = 0 ; j < N ; j ++) {
				dist = getDist(age[i][0], age[i][1], sta[j][0], sta[j][1]);
				res = min(res, dist);
			}
		}
		printf("%.3lf\n", res);
	}
	return 0;
}
