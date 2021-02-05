#include <bits/stdc++.h>
using namespace std;

// void allocate(double* dvalue) {
// 	if(!(dvalue = new double)) throw "No free space";
// }

// 动态分配一个变量的内存空间
void newElement() {
	// 使用 new 代替 malloc的好处：动态分配内存同时创建一个对象 可以被delete
	// new 得到一个指针 指向data type的一段内存空间
	// 存放在堆上
	double* dvalue = NULL;
	dvalue = new double;

	*dvalue = 123.4567;
	cout << "dvalue = " << *dvalue << endl;

	double* ddvalue = NULL;
	// 防止堆空间分配完毕
	try {
		// allocate(ddvalue);
		if(!(ddvalue = new double)) throw "No free space";
		*ddvalue = 765.4321;
		cout << "ddvalue = " << *ddvalue << endl;
	}
	catch(const char* msg) {
		cout << msg << endl;
	}

	// 注意delete掉动态分配的对象，防止内存泄漏

	delete dvalue;
	delete ddvalue;
}

// 动态分配1维数组
void newArray1() {
	char* str = new char[20];

	str[0] = 'a';
	str[1] = '\0';
	cout << "str = " << str << endl;

	// 1维数组的内存释放
	delete [] str;

	int m = 10;
	int* arr = new int[m];
	for(int i = 0 ; i < m ; i ++) {
		arr[i] = i + 1;
	}
	cout << "arr = ";
	for(int i = 0 ; i < m ; i ++) {
		cout << arr[i] << " ";
	}
	cout << endl;

	delete [] arr;
}

// 动态分配2维数组
void newArray2() {
	int m = 5, n = 10; // 第一维m, 第二维n
	// 非常关键！！！
	int** arr = new int*[m];
	for(int i = 0 ; i < m ; i ++) {
		arr[i] = new int[n];
	}
	cout << "2D array test begin:" << endl;
	for(int i = 0 ; i < m ; i ++) {
		for(int j = 0 ; j < n ; j ++) {
			arr[i][j] =  i + j;
		}
	}
	for(int i = 0 ; i < m ; i ++) {
		for(int j = 0 ; j < n ; j ++) {
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
	// 释放2维数组堆内存空间
	for(int i = 0 ; i < m ; i ++) {
		delete [] arr[i];
	}
	delete [] arr;
}

// 动态分配3维数组
void newArray3() {
	int m = 4, n = 3, h = 2; // 第一维m, 第二维n, 第3维h
	int*** arr = NULL;
	arr = new int**[m];
	for(int i = 0 ; i < m ; i ++) {
		arr[i] = new int*[n];
		for(int j = 0 ; j < n ; j ++) {
			arr[i][j] = new int[h];
		}
	}
	for(int i = 0 ; i < m ; i ++) {
		for(int j = 0 ; j < n ; j ++) {
			for(int k = 0 ; k < h ; k ++) {
				arr[i][j][k] = i + j + k;			}
		}
	}
	cout << "3D arr test begin" << endl;
	for(int i = 0 ; i < m ; i ++) {
		for(int j = 0 ; j < n ; j ++) {
			for(int k = 0 ; k < h ; k ++) {
				cout << arr[i][j][k] << " ";
			}
		}
		cout << endl;
	}

	// 释放3维数组堆内存空间
	for(int i = 0 ; i < m ; i ++) {
		for(int j = 0 ; j < n ; j ++) {
			delete [] arr[i][j];
		}
		delete [] arr[i];
	}
	delete [] arr;
}

class Box {
public:
	Box() {
		cout << "Box Constructed" << endl;
	}
	~Box() {
		cout << "Box Destructed" << endl;
	}
};

void newObject() {
	// 创建对象数组方式如下(创建单个对象 new Box 即可)
	Box* boxArr = new Box[3];

	delete [] boxArr;
}

int main(void) {
	newElement();
	newArray1();
	newArray2();
	newArray3();
	newObject();
	return 0;
}
