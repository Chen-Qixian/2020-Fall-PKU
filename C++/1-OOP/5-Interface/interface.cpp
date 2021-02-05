#include <bits/stdc++.h>
using namespace std;

// 使用C++实现接口：抽象类
class Shape {
protected:
	int height;
	int width;
public:
	// 有一个纯虚函数的类即位抽象类，它可以用来定义接口，但是必须在子类中实现该接口。
	virtual int area() = 0;
	void setHeight(int h) {
		height = h;
	}
	void setWidth(int w) {
		width = w;
	}
};

class Rectangle: public Shape {
public:
	Rectangle(int h=0, int w=0) {
		height = h;
		width = w;
	}
	virtual ~Rectangle() {}
	//必须在子类中实现该接口
	int area() {
		return height * width;
	}
};

class Triangle: public Shape {
public:
	Triangle(int h=0, int w=0) {
		height = h;
		width = w;
	}
	virtual ~Triangle() {}
	//必须在子类中实现该接口
	int area() {
		return height * width / 2;
	}
};

int main(void) {
	// 不能为抽象类直接实例化对象，否则编译错误。
	// Shape sp;
	// sp.setHeight(1);

	Rectangle rect;
	rect.setHeight(5);
	rect.setWidth(7);
	cout << rect.area() << endl;

	Triangle tri;
	tri.setHeight(18);
	tri.setWidth(7);
	cout << tri.area() << endl;
	return 0;
}
