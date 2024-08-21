#include "double_linked_list.h"

using namespace std;


DoubleLinkedList::DoubleLinkedList() {
    head = nullptr;
    tail = nullptr;
}

void DoubleLinkedList::Push(int val) {
    DoubleLinkedNode* new_node = new DoubleLinkedNode;
    new_node->value = val;
    if (head == nullptr) {
        head = new_node;
        tail = new_node;
    }
    else {
        tail->next = new_node;
        new_node->prev = tail;
        tail = tail->next;
    }
}

int DoubleLinkedList::Pop() {
    if (tail == head) {
        tail = nullptr;
        head = nullptr;
    }
    else {
        DoubleLinkedNode* temp = tail;
        tail = tail->prev;
        tail->next = nullptr;
        temp->prev = nullptr;
        temp = nullptr;
    }
}

vector<int> DoubleLinkedList::List() {
    vector<int> ans;
    DoubleLinkedNode* temp = head;
    while (temp != nullptr) {
        ans.push_back(temp->value);
        temp = temp->next;
    }
    return ans;
}

string DoubleLinkedList::Print() {
    vector<int> temp = DoubleLinkedList::List();
    string ans = "";
    for (int i : temp) {
        ans += to_string(i) + " ";
    }
    return ans;
}

void DoubleLinkedList::DelNode(int n) {
    DoubleLinkedNode* temp = head;
    while (n>1) {
        temp = temp->next;
        n--;
    }
    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    temp->next = nullptr;
    temp->prev = nullptr;
    temp = nullptr;
} 

void DoubleLinkedList::Reverse() {
    swap(head, tail);
    DoubleLinkedNode* temp = head;
    while(temp != nullptr) {
        swap(temp->next, temp->prev);
    }
}