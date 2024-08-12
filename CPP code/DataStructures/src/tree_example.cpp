#include "tree.h"

using namespace std;

int main() {
    BinarySearchTree t1(5);
    for (int i : {4,2,3,8,6,7}) {
        t1.insert(i);
    }
    LOG(LOG_LEVEL_INFO, "BFT of tree");
    for (int i : t1.BFT()) {
        LOG(LOG_LEVEL_INFO, "value : %d", i);
    } 
    LOG(LOG_LEVEL_INFO, "DFT of tree");
    for (int i : t1.DFT()) {
        LOG(LOG_LEVEL_INFO, "value : %d", i);
    }

    return 0;
}