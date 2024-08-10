#include "logger.h"
#include <vector>


class DoubleLinked {
    public:
        DoubleLinked();

        struct LinkedNode {
            int val;
            LinkedNode* prev = nullptr;
            LinkedNode* next = nullptr;
        };

        void push_front(int val);
        void push_back(int val);
        int pop_front();
        int pop_back();
        int front();
        int back();
        std::vector<int> list();

        std::vector<int> my_list;

        LinkedNode* head;
        LinkedNode* tail;
};