#include "stack.h"

using namespace std;

void Stack::push(int var) {
	arr.push_back(var);
}

int Stack::pop() {
	int popped = arr.back();
	arr.pop_back();
	return popped;
}

int Stack::top() {
	return arr.back();
}

bool Stack::is_empty() {
	return arr.size() == 0;
}