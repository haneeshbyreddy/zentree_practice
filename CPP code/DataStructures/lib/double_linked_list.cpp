#include "double_linked_list.h"

using namespace std;

DoubleLinked::DoubleLinked() {
    head = nullptr;
    tail = nullptr;
}

void DoubleLinked::push_back(int val) {
    LinkedNode* new_node = new LinkedNode;
    new_node->val = val;
    if (head == nullptr) {
        head = new_node;
        tail = new_node;
    }
    else {
        tail->next = new_node;
        LinkedNode* temp = tail;
        tail = tail->next;
        tail->prev = temp;
        temp = nullptr;
    }
}
void DoubleLinked::push_front(int val) {
    LinkedNode* new_node = new LinkedNode;
    new_node->val = val;
    if (head == nullptr) {
        head = new_node;
        tail = new_node;
    }
    else {
        new_node->next = head;
        head->prev = new_node;
        head = new_node;
    }
}
int DoubleLinked::pop_front() {
    if (head == nullptr) return -1;
    if (head == tail) {
        head = nullptr;
        tail = nullptr;
    }
    else {
        head = head->next;
        head->prev = nullptr;
    }
}
int DoubleLinked::pop_back() {
    if (head == tail) {
        head = nullptr;
        tail = nullptr;
    }
    else {
        tail = tail->prev;
        tail->next = nullptr;
    }
}
int DoubleLinked::front() {
    return head->val;
}
int DoubleLinked::back() {
    return tail->val;
}
vector<int> DoubleLinked::list() {
    my_list.clear();
    LinkedNode* temp = head;
    while (temp) {
        my_list.push_back(temp->val);
        temp = temp->next;
    }
    return my_list;
}