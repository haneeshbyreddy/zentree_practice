#include "logger.h"
#include <initializer_list>
#include <vector>
#include <string>

using namespace std;

class DoubleLinkedList {
    public:
        struct DoubleLinkedNode {
            int value;
            DoubleLinkedNode* next = nullptr;
            DoubleLinkedNode* prev = nullptr;
        };

        DoubleLinkedList();

        void Push(int val);
        int Pop();
        vector<int> List() const;
        string Print();
        void DelNode(int n);
        void Reverse();
        int Multiply(const DoubleLinkedList& dup);
        DoubleLinkedList QuickSort(bool inc);
        DoubleLinkedList MergeSort();

        DoubleLinkedNode* head;
        DoubleLinkedNode* tail;
};