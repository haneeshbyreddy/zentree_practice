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

vector<int> DoubleLinkedList::List() const {
    vector<int> ans;
    DoubleLinkedNode* temp = head;
    while (temp != nullptr) {
        ans.push_back(temp->value); temp = temp->next;
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
        temp = temp->next;
    }
}

int DoubleLinkedList::Multiply(const DoubleLinkedList& dup) {
    string one="", two="";
    for(int i : dup.List()) one += to_string(i);
    for(int i : DoubleLinkedList::List()) two += to_string(i);
    int one_i = stoi(one), two_i = stoi(two);
    return one_i * two_i;
}

DoubleLinkedList DoubleLinkedList::QuickSort(bool inc) {
    if (head == nullptr || head == tail) {
        return *this;
    }

    DoubleLinkedList l1, l2;
    DoubleLinkedNode* ref = new DoubleLinkedNode;
    ref->value = tail->value;

    DoubleLinkedNode* current = head;
    while (current != nullptr) {
        if (current->value < ref->value) {
            l1.Push(current->value);
        } else if (current != tail) {
            l2.Push(current->value);
        }
        current = current->next;
    }

    l1 = l1.QuickSort(inc);
    l2 = l2.QuickSort(inc);

    if (!inc) swap(l1, l2);

    if (l1.head != nullptr) {
        l1.tail->next = ref;
        ref->prev = l1.tail;
        l1.tail = ref;
    } else {
        l1.head = l1.tail = ref;
    }

    if (l2.head != nullptr) {
        ref->next = l2.head;
        l2.head->prev = ref;
        l1.tail = l2.tail;
    } else {
        l1.tail = ref;
    }

    return l1;
}