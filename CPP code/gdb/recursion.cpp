#include <iostream>
#include <format>
using namespace std;

int recursion(int num) {
	return num * recursion(num - 1);
}

int main() {
	int var = 4;
	int factorial = recursion(4);
	cout << format("factorial of {} is {}", var, factorial) << endl;
	return 0;
}
