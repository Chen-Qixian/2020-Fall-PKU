#include <bits/stdc++.h>
using namespace std;

class Shape{
protected:
	int width;
	int height;
public:
	int getWidth() {
		return width;
	}
	int getHeight() {
		return height;
	}
	void setWidth(int w) {
		width = w;
	}
	void setHeight(int h) {
		height = h;
	}
	// Shape(){}
	// ~Shape();
};

class Cost{
protected:
	int cost;
public:
	int getCost(int area) {
		return area * cost;
	}
	void setCost(int c) {
		cost = c;
	}
	// Cost(){}
	// ~Cost();
};

// 多继承自两个基类
class Rectangular: public Shape, public Cost{
public:
	int getArea() {
		return width * height;
	}
	// Rectangular(){}
	// ~Rectangular();
};


int main(void) {
	Rectangular r;
	r.setHeight(10);
	r.setWidth(60);
	int area = r.getArea();
	r.setCost(5);
	int total = r.getCost(area);
	cout << area << " " << total << endl;
	return 0;
}
