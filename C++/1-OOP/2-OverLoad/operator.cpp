#include <iostream>
using namespace std;

const int SIZE = 10;

class Distance{
private:
	int feet;
	int inches;
public:
	Distance(){}
	Distance(int f, int i): feet(f), inches(i) {}

	void showDist() {
		cout << "F: " << feet << " I:" << inches << endl;
	}
	// 重载一元运算符
	Distance operator- () {
		feet = -feet;
		inches = - inches;
		return Distance(feet, inches);
	}
	// 重载关系运算符
	bool operator< (const Distance& d) {
		return (feet < d.feet) ? true: (feet == d.feet && inches < d.inches) ? true: false;
	}
	// 重载IO：声明为友元函数，可以不声明对象而直接调用
	friend ostream &operator<< (ostream& output, Distance& d) {
		output << "F: " << d.feet << " I: " << d.inches << endl;
		return output;
	}

	friend istream &operator>> (istream& input, Distance& d) {
		input >> d.feet >> d.inches;
		return input;
	}
	// 重载调用运算符
	Distance operator() (int a, int b, int c) {
		Distance D;
		// 随机运算
		D.feet = a + b + c;
		D.inches = a + b + 100;
		return D;
	}
};


// 重载二元运算符
class Box{
private:
	int length;
	int height;
	int width;
public:
	Box(){}
	Box(int l, int h, int w): length(l),height(h),width(w){}
	// 将 - 号后边的对象传递给 b
	Box operator- (const Box& b) {
		Box ret;
		ret.length = length - b.length;
		ret.height = height - b.height;
		ret.width  = width  - b.width;
		return ret;
	}
	int getVolume() {
		return length * height * width;
	}
};


// 重载++运算符
class Time{
private:
	int minute;
	int hour;
public:
	Time(): minute(0), hour(0) {}
	Time(int h, int m) {
		minute = m;
		hour = h;
	}

	void showTime() {
		cout << "H: " << hour << " M: " << minute << endl;
	}
	// 重载前缀++运算符
	Time operator++ () {
		minute ++;
		if(minute == 60) {
			minute = 0;
			hour ++;
		}
		return Time(hour, minute);
	}
	// 重载后缀++运算符：返回原来的对象
	Time operator++ (int) {
		Time T(hour, minute);
		minute ++;
		if(minute == 60) {
			minute = 0;
			hour ++;
		}
		return T;
	}
};

// 重载[]运算符
class SafeArray{
	int arr[SIZE];
public:
	SafeArray() {
		for(int i = 0 ; i < SIZE ; i ++) {
			arr[i] = i;
		}
	}
	// 保证不越界
	int& operator[] (int idx) {
		if(idx >= SIZE) {
			cout << "index overflow" << endl;
			return arr[0];
		}
		return arr[idx];
	}
};

int main(void) {
	// 一元重载
	Distance d1(10,200);
	Distance d2(-10,500);
	-d1;
	d1.showDist();
	-d2;
	d2.showDist();
	// 关系重载
	if(d1 < d2) cout << "d1 < d2" << endl;
	else cout << "d1 > d2" << endl;
	// IO 重载
	cout << "Input value of Object" << endl;
	Distance d3;
	cin >> d3;
	cout << "###D3" << endl;
	cout << "1st distance: " << d1;
	cout << "2nd distance: " << d2;
	cout << "3rd distance: " << d3;
	// 二元重载
	Box b1(1,2,3);
	Box b2(3,4,5);
	Box b3 = b1 - b2;
	cout << b1.getVolume() << endl;
	cout << b2.getVolume() << endl;
	cout << b3.getVolume() << endl;
	// ++运算符重载
	Time t1(1, 2);
	(++ t1).showTime();
	(++ t1).showTime();

	Time t2(1, 59);
	(t2 ++).showTime();
	(t2 ++).showTime();
	// 函数调用重载
	Distance d4 = d3(10, 10, 10);
	d4.showDist();
	// []运算符重载
	SafeArray sa;
	cout << sa[1] << endl;
	cout << sa[10] << endl;
	return 0;
}
