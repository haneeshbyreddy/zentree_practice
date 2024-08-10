#include "logger.h"
#include <vector>

class Queue {

    public:
        void push(int var);
        int pop();
        int front();
    private:
        std::vector<int> queue;
};