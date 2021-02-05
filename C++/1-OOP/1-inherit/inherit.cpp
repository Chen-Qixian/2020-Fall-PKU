#include<iostream>
using namespace std;

class Shape {
protected:
	int width;
	int height;
public:
	void setHeight(int h) {
		height = h;
	}

	void setWidth(int w) {
		width = w;
	}
};

class Rectangle: public Shape {
public:
	int area() {
		return height * width;
	}
};

class Square: public Rectangle {
public:
	int getWidth() {
		return width;
	}
};

int main() {

	Rectangle r;
	r.setHeight(4);
	r.setWidth(5);
	cout << r.area() << endl;

	Square s;
	s.setWidth(10);
	cout << s.getWidth() << endl;

	return 0;
}
