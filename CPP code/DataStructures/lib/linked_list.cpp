#include "linked_list.h"
#include <vector>
#include <iostream>

using namespace std;


LinkedList::LinkedList() {
	head = nullptr;
	tail = nullptr;
}

void LinkedList::push_front(int val) {
	LinkedNode* new_node = new LinkedNode;
	new_node->val = val;
	new_node->next = head;
	head = new_node;
	if (tail == nullptr) {
		tail = new_node;
	}
}

void LinkedList::push_back(int val) {
	LinkedNode* new_node = new LinkedNode;
	new_node->val = val;
	if (head == nullptr) {
		head = new_node;
		tail = new_node;
	}
	else {
		tail->next = new_node;
		tail = new_node;
	};
}

int LinkedList::pop_front() {
	if (head == nullptr) {
		return -1;
	}
	int temp = head->val;
	head = head->next;
	return temp;
}

int LinkedList::pop_back() {
	if (head == nullptr) {
		return -1;
	}
	LinkedNode* temp = head;
	while (temp->next != tail) {
		temp = temp->next;
	}
	temp->next = nullptr;
	int popped = tail->val;
	tail = temp;
	return popped;
}

int LinkedList::front() {
	return head->val;
}

int LinkedList::back() {
	return tail->val;
}

vector<int> LinkedList::list() {
	vector<int> ans;
	LinkedNode* temp = head;
	while (temp) {
		ans.push_back(temp->val);
		cout << temp->val << endl;
		temp = temp->next;
	}
	return ans;
}