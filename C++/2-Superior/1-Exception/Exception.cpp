#include <bits/stdc++.h>
using namespace std;

double division(double a, double b) {
	// 抛出一个异常
	if(b == 0) throw "Divided by zero";
	return a / b;
}

// 自定义异常类
struct MyException: public exception {
	const char* what() const throw() {
		return "My Exception!\n";
	}
};

int main(void) {
	try {
		cout << division(10.0, 21.0) << endl;
	}
	// 类型const char* 必须和throw的一致
	catch (const char* msg) {
		cout << msg << endl;
	}

	try {
		cout << division(10.0, 0) << endl;
	}
	catch(const char* msg) {
		cout << msg << endl;
	}

	try {
		throw exception();
	}
	catch(exception& e) {
		// what是异常类的公共方法，可以返回抛出异常的原因
		cout << e.what() << endl;
	}

	try {
		throw MyException();
	}
	catch(MyException& e) {
		cout << e.what() << endl;
	}
	catch(exception& e) {
 		cout << "Other Exception" << endl;
	}


	return 0;
}
