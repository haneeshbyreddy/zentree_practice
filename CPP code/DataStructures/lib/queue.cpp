#include "queue.h"

using namespace std;

// class Queue {

//     public:
//         void PushItem(int var) {
//             queue.push_back(var);
//         }
//         int PopItem() {
//             if (queue.empty()) {
//                 return -1;
//             };
//             int front = queue.front();
//             queue.erase(queue.begin());
//             return front;
//         }
//         int FrontItem() {
//             return queue.front();
//         }
//     private:
//         vector<int> queue;
// };

void Queue::push(int var) {
    queue.push_back(var);
}

int Queue::pop() {
    if (Queue)
}