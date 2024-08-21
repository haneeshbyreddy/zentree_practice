#include "double_linked_list.h"

using namespace std;

int main() {
    DoubleLinkedList dl;
    for (int i : {1,2,3,4,5}) {
        dl.Push(i);
    }
    dl.DelNode(3);
    LOG(LOG_LEVEL_INFO, "%s", dl.Print().c_str());
}