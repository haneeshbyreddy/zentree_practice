#include <thread>
#include <iostream>
#include <chrono>
using namespace std;

int var = 0;

void increase(int* num) {
	for (int i=0;i<1000;i++) {
		(*num)++;
		this_thread::sleep_for(chrono::milliseconds(5));
	}
}
int main() {
	thread t1(increase, &var);
	thread t2(increase, &var);
	thread t3(increase, &var);
	t1.join();
	t2.join();
	t3.join();
	cout << var << endl;
	return 0;
}

