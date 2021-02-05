#include <bits/stdc++.h>
using namespace std;

// 枚举型变量，默认比前面值大1，可以为其中的某个标识符赋值
enum color {red, green, blue};
enum newcolor {yellow, orange = 5, purple};

// 变量的声明：声明的同时可以定义，但定义在同一作用域只能有一次
// 变量只允许被定义一次，但可以在其他文件中多次声明
// extern作用于函数，则声明函数可被外部调用
extern int a, b;

// static存储类：被声明为static的全局变量作用域被限制为当前文件
// 被声明为static的局部变量，在每次函数调用时不会重新创建和销毁，而会保留该变量的值
// 类中被声明为static的成员变量，会使得只有一个该成员的副本被所有对象共享
static int cnt = 3;
void counter() {
	static int num = 0;
	num ++;
	cout << num << " ";
}
class Counter{
	// 静态成员变量只能在此声明，定义必须单独进行（在下面）
	static int num;
public:
	Counter() {
		// int num = 0; 【错误】不能在构造函数中为静态成员变量赋值，必须在类外部初始化一个赋值
	}
	~Counter() {}
	int getNum() {
		return num;
	}
	void addNum(int x) {
		num += x;
	}
};

int Counter::num = 0;

// 传值调用函数：形参为拷贝的副本，并不会真正改变被交换的两个数
void swap1(int a, int b) {
	int t = a;
	a = b;
	b = t;
}
// 传指针调用函数：需要修改指针中的内容，会真正改变被交换的两个数
void swap2(int* a, int* b) {
	int t = *a;
	*a = *b;
	*b = t;
}
// 传引用调用函数：需要修改指针中的内容，会真正改变被交换的两个数
void swap3(int& a, int& b) {
	int t = a;
	a = b;
	b = t;
}

// 向函数传递数组：指针传递、指定数组大小、不指定数组大小
// double getAvg(int a[10], int size)
// double getAvg(int a[], int size)
double getAvg(int* a, int size) {
	double sum = 0.0;
	for(int i = 0 ; i < size ; i ++) {
		sum += a[i];
	}
	return sum / size;
}

void addPtr() {
	cout << "test int ptr begin:" << endl;
	int a[5] = {1,2,3,4,5};
	int* p = a;
	for(int i = 0 ; i < 5 ; i ++) {
		cout << "Address is: " << p << endl;
		cout << "num is:" << *p << endl;
		p ++;
	}
	cout << "test char ptr begin:" << endl;
	char c[6] = "hello";
	char* q = c;
	for(int i = 0 ; i < 5 ; i ++) {
		cout << "Address is: " << q << endl;
		cout << "char is:" << *q << endl;
		q ++;
	}
}
// 返回指针的函数
int* getRandArr() {
	// 不能向函数外部返回一个局部变量，除非声明为static
	static int ret[10];
	srand((unsigned) time(NULL));
	for(int i = 0 ; i < 10 ; i ++) {
		ret[i] = rand() % 100;
	}
	return ret;
}
// 返回引用的函数
int refArr[10] = {0,1,2,3,4,5,6,7,8,9};
int& modifyRef(int x) {
	return refArr[x];
}

int main(void) {
	int a, b; // 变量的定义 (会覆盖掉extern的声明)
	a = 1;
	b = 2;
	cout << "test var declare & definition begin:" << endl;
	cout << a << " " << b <<  endl;
	cout << "test enum begin:" << endl;
	color c = blue;
	cout << c << " ";
	newcolor d = purple;
	cout << d << endl;
	cout << "test var sign begin:" << endl;
	short e;
	unsigned short f;
	f = 50000;
	e = f;
	cout << e << " " << f << endl;
	// volatile保证了对特定内存的稳定访问，阻止编译器对该变量访问的优化
	volatile int g = 1;
	// 若中间对g🈚️操作，则编译器优化后不直接从g对应的内存空间中取g的值
	cout << "test volatile begin:\n" << g << endl;
	// restrict 限制的指针，指针是其唯一访问方式，仅限C++99
	// restrict int* x;
	// restrict int* y;
	// *x = 1;
	// *y = 2;
	// *x = *y;
	// cout << "test restrict begin:\n" << *x << endl;
	cout << "test static var begin:\n";
	while(cnt --) counter();
	cout << "test static object begin:\n";
	Counter h1;
	h1.addNum(1);
	cout << h1.getNum() << " ";
	Counter h2;
	h2.addNum(3);
	cout << h2.getNum() << endl;
	// 取地址运算符& 和间接寻址运算符*
	int i = 10;
	int* j;
	int k;
	j = &i;
	cout << "test pointer begin:\n" << *j << endl;

	// 函数调用：参数传递方式：值传递、传指针、传引用
	// 1、传值：形参相当于拷贝一份传递值的副本
	int l = 1, m = 2;
	swap1(l, m);
	cout << l << " " << m << endl;
	// 2、传指针，那么就需要讲两个数的地址作为参数传入
	swap2(&l, &m);
	cout << l << " " << m << endl;
	// 3、传引用，形参就是传入的变量
	swap3(l, m);
	cout << l << " " << m << endl;
	// 生成随机数:
	// rand()会根据种子seed产生一个数，seed默认为1
	// srand((unsigned) time(NULL) )则会根据当前时间修改种子 seed的值，实现随机
	// 为了生成区间[m,n)之间的随机数，可用公式rand() % (n-m) + m;
	// 为了生存区间[0,1)之间的浮点型随机数，可以采用rand() % n / (n + 1)，其中使用n 控制精度，n=99则有2位小数，n=999则有3位小数
	cout << "test random begin:\n";
	srand((unsigned) time (NULL));
	for(int i = 0 ; i < 10 ; i ++) {
		cout << rand() % 10 + 10 << " ";
	}
	cout << endl;
	for(int i = 0 ; i < 10 ; i ++) {
		cout << rand() % 9999 * 1.0 / 10000.0 << " ";
	}
	int n[10] = {1,2,3,4,5,6,7,8,9,10};
	int *o = n;
	cout << "test array pointer begin:\n";
	cout << *o << " " << *(o+1) << " " << *(o+9) << endl;
	// 向函数传递数组
	cout << getAvg(n, 10) << endl;

	int* p;
	int q = 20;
	p = &q;
	cout << "q address is: " << p << "\nvalue of *p is: " << *p << endl;
	// 指针的自增：int 型指针地址自增4，char型自增1
	addPtr();
	// 使用指针访问数组
	int r[10] = {0,1,2,3,4,5,6,7,8,9};
	cout << "test array name as pointer begin:\n";
	for(int i = 0 ; i < 10 ; i ++) {
		cout << *(r + i) << " ";
	}
	// 指针数组
	int* s[10];
	cout << "\ntest pointer array begin:\n";
	for(int i = 0 ; i < 10 ; i ++) {
		s[i] = &r[i];
	}
	for(int i = 0 ; i < 10 ; i ++) {
		cout << *s[i] << " ";
	}
	// 从函数返回指针
	int* t;
	t = getRandArr();
	cout << "\ntest pointer returned from function begin:\n";
	for(int i = 0 ; i < 10 ; i ++) {
		cout << *(t + i) << " ";
	}
	// 引用：指向被引用的变量
	// 引用与指针的区别：
	// 1、引用一旦定义就不能改变，指向对象后不能改变为其他对象
	// 2、引用不能指向空，必须连接到一块合法内存
	// 3、引用必须在创建时初始化
	int u;
	int& v = u;
	u = 20;
	cout << "\ntest reference begin:\n";
	cout << "reference number:" << v << endl;
	modifyRef(2) = 12;
	cout << "test function reference begin:\n";
	cout << refArr[2] << endl;

	return 0;
}
