#include <bits/stdc++.h>
using namespace std;

class Output{
public:
	void print(int x) {
		cout << x << endl;
	}
	void print(double x) {
		cout << x << endl;
	}
	void print(char x) {
		cout << x << endl;
	}
	void print(string x) {
		cout << x << endl;
	}
};

int main(void) {
	Output out;
	out.print(1);
	out.print(3.224);
	out.print('0');
	out.print("hello world");
	return 0;
}
