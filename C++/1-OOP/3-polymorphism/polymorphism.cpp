#include <iostream>
using namespace std;

class Shape {
protected:
	int width;
	int height;
public:
	Shape(int w, int h) {
		width = w;
		height = h;
	}
	// 基类析构写成虚函数 以免被覆盖掉
	virtual ~Shape() {}
	// 若不使用virtual 则造成静态多态/静态链接：早绑定
	// virtual 是实现多态的方式
	// 这样为基类指针赋值子类对象地址时，可以访问子类对象的成员
	// virtual int area() {
	// 	cout << "parent called" << endl;
	// 	return width * height * 2;
	// }
	// 若父类中不能给出有意义的虚函数实现，可以写成纯虚函数的形式

	virtual int area() = 0;
	// 其中=0表示该函数没有主体
};

class Rectangle: public Shape {
public:
	Rectangle(int w, int h): Shape(w, h) {}
	virtual ~Rectangle() {}
	int area() {
		cout << "Rectangle called" << endl;
		return width * height;
	}
};

class Triangle: public Shape {
public:
	Triangle(int w, int h): Shape(w, h) {}
	virtual ~Triangle() {}
	int area() {
		cout << "Triangle called" << endl;
		return width * height / 2;
	}

};

int main(void) {
	Shape* shape;
	Rectangle rect(5, 6);
	shape = &rect;
	shape->area();

	Triangle tri(7, 8);
	shape = & tri;
	shape->area();


	return 0;
}
