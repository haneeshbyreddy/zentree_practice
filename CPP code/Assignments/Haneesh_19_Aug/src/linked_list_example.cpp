#include "linked_list.h"
#include <initializer_list>

using namespace std;

int main() {
    LOG(LOG_LEVEL_INFO, "======= Single Linked list =======");

    LinkedList list;
    list.MakeList({1,2,5,7,8,9});
    LOG(LOG_LEVEL_INFO, "tail value : %d", list.TailVal());
    LOG(LOG_LEVEL_INFO, "list count : %d", list.Count());
    list.Push(11);
    LOG(LOG_LEVEL_INFO, "tail value : %d", list.TailVal());
    LOG(LOG_LEVEL_INFO, "list count : %d", list.Count());
    list.DeleteNode(list.NthNode(2));
    LOG(LOG_LEVEL_INFO, "tail value : %d", list.TailVal());
    LOG(LOG_LEVEL_INFO, "list count : %d", list.Count());
    
    LOG(LOG_LEVEL_INFO, "======= Stack using Linked list =======");

    LinkedList stack;
    for(int i : {1,2,3,4}) {
        list.PushFront(i);
    }
    LOG(LOG_LEVEL_INFO, "popped %d from stack", list.PopFront());
    LOG(LOG_LEVEL_INFO, "popped %d from stack", list.PopFront());
    LOG(LOG_LEVEL_INFO, "popped %d from stack", list.PopFront());
    list.PushFront(7);
    LOG(LOG_LEVEL_INFO, "popped %d from stack", list.PopFront());

    LOG(LOG_LEVEL_INFO, "======= Swapping nodes in linked list =======");

    LinkedList swap_list;
    swap_list.MakeList({1,2,3,4,5,6,7,8,9});
    LOG(LOG_LEVEL_INFO, "Before swap : %s", swap_list.PrintList().c_str());
    swap_list.SwapNode();
    LOG(LOG_LEVEL_INFO, "After swap : %s", swap_list.PrintList().c_str());
}

