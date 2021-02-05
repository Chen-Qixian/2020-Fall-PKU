#include <bits/stdc++.h>
using namespace std;


// 嵌套的命名空间
namespace firstNamespace {
	void func() {
		cout << "inside first namespace" << endl;
	}
	namespace secondNamespace {
		void func() {
			cout << "inside second namespace" << endl;
		}
	}
}

// 使用嵌套的命名空间
using namespace firstNamespace::secondNamespace;
int main(void) {
	func();
	return 0;
}
