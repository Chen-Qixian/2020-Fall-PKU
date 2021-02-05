#include <bits/stdc++.h>
using namespace std;

struct pair_hash {
	template<class T1, class T2>
	size_t operator () (pair<T1, T2> const& pair) const {
		size_t h1 = hash<T1>()(pair.first);
		size_t h2 = hash<T2>()(pair.second);
		return h1 ^ h2;
	}
};

int main(void) {
	unordered_set<pair<string, int>, pair_hash> st =
	{
		{"one", 1},
		{"two", 2},
		{"three", 3},
		{"four", 4}
	};
	for(auto it = st.begin(); it != st.end(); it ++) {
		cout << it->first << " : " << it->second << endl;
	}
	return 0;
}
