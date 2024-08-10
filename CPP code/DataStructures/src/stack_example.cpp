#include "stack.h"

using namespace std;

int main() {
    Stack stack;
    for(int i : {1,3,5,6,8}) {
        stack.push(i);
        LOG(LOG_LEVEL_INFO, "pushed item %d", i);
    }
    while(!stack.is_empty()) {
        LOG(LOG_LEVEL_INFO, "popped item %d", stack.pop());
    }
    LOG(LOG_LEVEL_INFO, "stack is empty : %d", stack.is_empty());
}