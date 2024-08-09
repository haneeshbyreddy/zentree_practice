#include "logger.h"
#include <initializer_list>

using namespace std;

struct ListNode {
    int val;
    ListNode* prev = nullptr;
    ListNode* next = nullptr;
};

int main() {
    ListNode* head = nullptr;
    ListNode* tail = nullptr;

    LOG(LOG_LEVEL_INFO, "Creating the double linked list");
    for (int i : {1,2,4,5,7,8}) {
        ListNode* new_node = new ListNode;
        new_node->val = i;
        if (head == nullptr) {
            head = new_node;
            tail = new_node;
        }
        else {
            tail->next = new_node;
            ListNode* temp = tail;
            tail = tail->next;
            tail->prev = temp;
            temp = nullptr;
        }
    }

    LOG(LOG_LEVEL_INFO, "Traversing the double linked list");
    ListNode* curr = head;
    while (curr != nullptr) {
        LOG(LOG_LEVEL_INFO, "Current Node value : %d", curr->val);
        curr = curr->next;
    }

    LOG(LOG_LEVEL_INFO, "Reverse traversing the double linked list");
    curr = tail;
    while (curr != nullptr) {
        LOG(LOG_LEVEL_INFO, "Current Node value : %d", curr->val);
        curr = curr->prev;
    }

    return 0;
}