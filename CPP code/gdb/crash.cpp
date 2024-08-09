#include <iostream>

using namespace std;

void update_i(int* i) {
	cout << "updating the value of i" << endl;
	*i = 1;
}

int main() {
    int var = 10;
    for (int i=0;i<10;i++) {
	    var -= 1;
    }
    int* i = nullptr;
    update_i(i);
    return 0;
}

