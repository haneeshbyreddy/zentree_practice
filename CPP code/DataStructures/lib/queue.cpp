#include "queue.h"

using namespace std;

void Queue::push(int var) {
    queue.push_back(var);
}

int Queue::pop() {
    if (queue.empty()) return -1;
    int front = queue.front();
    queue.erase(queue.begin());
    return front;

}

int Queue::front() {
    return queue.front();
}