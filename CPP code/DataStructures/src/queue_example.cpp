#include "queue.h"

int main() {
    Queue queue;
    for (int i : {1,2,3,4,5}) {
        queue.push(i);
    }
    LOG(LOG_LEVEL_INFO, "popped element %d", queue.pop());
    LOG(LOG_LEVEL_INFO, "front element %d", queue.front());
}