#include <bits/stdc++.h>
using namespace std;

// 使用 模板编程->泛型编程 可以独立于任何特定的数据类型进行编程
// 函数模板
template <typename T>
inline T const& Max(T const& a, T const& b) {
	return a > b ? a: b;
}

// 类模板
template <class T>
class Stack {
	vector<T> v;
public:
	Stack () {}
	~Stack() {}
	// 写法1:
	// void push(T elem) {
	// 	v.push_back(elem);
	// }
	// 写法2:
	// void push(T elem);
	// 写法3: 推荐
	void push(T const&);

	void pop(){
		if(empty()) throw out_of_range("Stack<>::pop() Empty stack!");
		v.pop_back();
	}

	T top() const;

	// const成员函数：保证不会修改类内部成员，以及不会调用其他非const成员函数
	bool empty() const{
		return (v.size() == 0);
	}
};

// 注意传入参数如果在函数内部不改动最好传递const&
template <class T>
void Stack<T>::push(T const& elem) {
	v.push_back(elem);
}

// const成员函数
template <class T>
T Stack<T>::top() const {
	if(empty()) throw out_of_range("Stack<>::top() Empty stack!");
	return v.back();
}

int main(void) {
	// 使用定义的函数模板 可以向其中传递不同类型的数据
	int a = 12, b = 39;
	cout << "Int max: " << Max(a, b) << endl;

	double c = 1.234, d = 0.025;
	cout << "double max: " << Max(c, d) << endl;

	string e = "iiejd", f = "iiejdq";
	cout << "string max: " << Max(e, f) << endl;

	// 使用类模板构造对象
	try {
		cout << "Create int stack" << endl;
		Stack<int> intStack;
		intStack.push(7);
		intStack.push(9);
		cout << "get number: " << intStack.top();
		intStack.pop();
		cout << " " << intStack.top();
		intStack.pop();

		cout << "\nCreate String stack" << endl;
		Stack<string> stringStack;
		stringStack.push("world");
		stringStack.push("hello");
		cout << "get string: " << stringStack.top();
		stringStack.pop();
		cout << " " << stringStack.top();
		stringStack.pop();
		stringStack.pop();
	}
	catch (exception& e) {
		// 通用的异常显示方法
		cerr << "\nException: " << e.what() << endl;
		return -1;
	}

	return 0;
}
