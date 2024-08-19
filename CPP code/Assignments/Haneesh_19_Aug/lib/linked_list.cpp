#include "linked_list.h"

using namespace std;

LinkedList::LinkedList() {
    head = nullptr;
    tail = nullptr;
};

void LinkedList::MakeList(initializer_list<int> list) {
    for (int i : list) {
        Push(i);
    }
}

void LinkedList::Push(int value) {
    ListNode* new_node = new ListNode;
    new_node->value = value;
    if (head == nullptr) {
        head = new_node;
        tail = new_node;
    }
    else {
        tail->next = new_node;
        tail = tail->next;
    }
}

int LinkedList::TailVal() {
    return tail->value;
}

int LinkedList::Count() {
    int count = 0;
    ListNode* temp = head;
    while (temp != nullptr) {
        temp = temp->next;
        count += 1;
    }
    return count;
}

vector<int> LinkedList::ListValues() {
    vector<int> val_arr;
    ListNode* temp = head;
    while (temp != nullptr) {
        val_arr.push_back(temp->value);
        temp = temp->next;
    }
    return val_arr;
}

string LinkedList::PrintList() {
    string values = "";
    for (int i : ListValues()) {
        values += to_string(i);
        values += " ";
    }
    return values;
}

LinkedList::ListNode* LinkedList::NthNode(int val) {
    ListNode* temp = head;
    while(val>0) {
        temp = temp->next;
        val--;
    }
    return temp;
}

void LinkedList::DeleteNode(ListNode* node) {
    while (node->next != tail) {
        node->value = node->next->value;
        node = node->next;
    }
    tail = node;
    tail->next = nullptr;
}

void LinkedList::PushFront(int val) {
    ListNode* temp = new ListNode;
    temp->value = val;
    if (head == nullptr) {
        head = temp;
        tail = temp;
    }
    else {
        temp->next = head;
        head = temp;
    }
}

int LinkedList::PopFront() {
    if (Count() == 0) {
        return -1;
    }
    int top_value = head->value;
    head = head->next;
    if (head == nullptr) {
        tail = nullptr;
    }
    return top_value;
}

void LinkedList::SwapNode() {
    ListNode* p1 = head;
    ListNode* p2 = head->next;
    ListNode* temp = new ListNode;
    if (head != tail) {
        head = head->next;
    }

    while (p1 != nullptr && p2 != nullptr) {
        p1->next = p2->next;
        p2->next = p1;
        temp->next = p2;
        temp = p1;
        p1 = p1->next;
        if (p1 != nullptr) p2 = p1->next;
    }
}