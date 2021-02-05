#include <bits/stdc++.h>
using namespace std;

// 命名空间：在函数名前增加命名空间区分同名函数

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

int main(void) {
	firstNamespace::func();
	secondNamespace::func();
	return 0;
}
