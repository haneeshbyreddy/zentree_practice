#include "logger.h"
#include <vector>

class Stack {
    public:
        void push(int var);
        int pop();
        int top();
        bool is_empty();
    private:
        std::vector<int> arr;
};