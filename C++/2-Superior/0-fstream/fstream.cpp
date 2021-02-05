#include <iostream>
#include <fstream>
using namespace std;

int main(void) {
	// 打开文件，防止已存在，采用截取模式trunc
	ofstream outfile;
	outfile.open("newfile.txt", ios::out | ios::trunc);
	// 简化版写法
	// outfile.open("test.tet");

	char name[500];
	cout << "Writing to the file" << endl;
	cout << "Input your name: ";
	cin.getline(name, 100);
	outfile << name << endl;

	int age;
	cout << "Enter your age: ";
	cin >> age;
	outfile << age << endl;

	// 打开文件，可以读写
	ifstream afile;
	afile.open("newfile.txt", ios::out | ios::in);
	// 只读文件
	// ifsteam inFile;
	// inFile.open("text.txt");
	string rname;
	cout << "Reading from the file" << endl;
	// 注意每次读出的内容以空格作为截断
	afile >> rname;
	cout << "read name: " << rname << endl;

	// 文件查找指针
	afile.seekg(4);

	int rage;
	afile >> rage;
	cout << "read age: " << rage << endl;

	// 程序终止前需手动关闭所有打开的文件
	outfile.close();
	afile.close();
	return 0;
}
