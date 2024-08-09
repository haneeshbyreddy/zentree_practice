#include "logger.h"
#include <vector>

using namespace std;

class LinkedList {
    public:
        LinkedList();

        struct LinkedNode {
            int val;
            LinkedNode* next;
        };

        void push_front(int val);
        void push_back(int val);
        int pop_front();
        int pop_back();
        int front();
        int back();
        vector<int> list();

        LinkedNode* head;
        LinkedNode* tail;
};