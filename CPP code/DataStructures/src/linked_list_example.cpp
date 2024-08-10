#include "linked_list.h"
#include <initializer_list>
#include <string>

using namespace std;

int main() {
    LinkedList list;
    for (int i : {1,2,3,4}) {
        list.push_back(i);
        LOG(LOG_LEVEL_INFO, "inserted item %d to back", list.back());
    }

    list.list();
    return 0;
}