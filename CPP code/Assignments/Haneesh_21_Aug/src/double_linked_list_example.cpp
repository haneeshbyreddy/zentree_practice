#include "double_linked_list.h"

using namespace std;

int main() {
    DoubleLinkedList dl;
    for (int i : {1,2,3,4,5}) {
        dl.Push(i);
    }
    dl.DelNode(3);
    LOG(LOG_LEVEL_INFO, "%s", dl.Print().c_str());
    dl.Reverse();
    LOG(LOG_LEVEL_INFO, "%s", dl.Print().c_str());

    DoubleLinkedList dl_1, dl_2;
    for (int i : {3,2}) dl_1.Push(i);
    for (int i : {2}) dl_2.Push(i);
    LOG(LOG_LEVEL_INFO, "Multiplication is %d", dl_1.Multiply(dl_2));

    DoubleLinkedList dl_3;
    for (int i : {5,3,6,8,2,9}) dl_3.Push(i);

    DoubleLinkedList dl_3_quicksorted = dl_3.QuickSort(true);
    LOG(LOG_LEVEL_INFO, "QuickSorted array : %s", dl_3_quicksorted.Print().c_str());

    DoubleLinkedList dl_3_mergesorted = dl_3.MergeSort();
    LOG(LOG_LEVEL_INFO, "QuickSorted array : %s", dl_3_mergesorted.Print().c_str());

}