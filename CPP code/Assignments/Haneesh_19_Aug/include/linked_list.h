#include "logger.h"
#include <vector>
#include <string>

using namespace std;

class LinkedList {
    public:
        LinkedList();

        struct ListNode {
            int value;
            ListNode* next = nullptr;
        };

        void MakeList(initializer_list<int> list);
        void Push(int value);
        int TailVal();
        int Count();
        void DeleteNode(ListNode* node);
        ListNode* NthNode(int val);
        void PushFront(int val);
        int PopFront();
        void SwapNode();
        vector<int> ListValues();
        string PrintList();

        ListNode* head;
        ListNode* tail;
};