#include "logger.h"
#include <vector>

class Queue {

    public:
        void push(int var);
        int pop();
        int FrontItem();
    private:
        std::vector<int> queue;
};