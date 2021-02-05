#include <bits/stdc++.h>
using namespace std;

namespace firstNamespace {
	void func() {
		cout << "inside first namespace" << endl;
	}
}

namespace secondNamespace {
	void func() {
		cout << "inside second namespace" << endl;
	}
}

// 使用某具体的命名空间
using namespace firstNamespace;
int main(void) {
	func();
	return 0;
}
