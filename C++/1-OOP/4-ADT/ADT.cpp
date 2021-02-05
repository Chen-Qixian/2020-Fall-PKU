#include <iostream>
using namespace std;

class Adder {
private:
	int total;
public:
	Adder(int i = 0) {
		total = i;
	}
	virtual ~Adder() {}

	void addNum(int num) {
		total += num;
	}

	int getTotal() {
		return total;
	}
};

int main(void) {
	Adder add(10);
	add.addNum(12);
	cout << add.getTotal() << endl;
	return 0;
}
