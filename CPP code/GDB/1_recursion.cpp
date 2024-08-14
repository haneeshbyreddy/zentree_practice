#include <iostream>
using namespace std;

int recursion(int num) {
	return num * recursion(num - 1);
}

int main() {
	int var = 4;
	int factorial = recursion(var);
	cout << "factorial of " << var << " is " << factorial << endl; 
	return 0;
}


