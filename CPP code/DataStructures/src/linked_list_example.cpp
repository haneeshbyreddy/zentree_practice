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
    list.push_front(9);
    LOG(LOG_LEVEL_INFO, "inserted item %d at front", list.front());
    LOG(LOG_LEVEL_INFO, "poped item %d at back", list.pop_back());
    list.push_back(7);
    LOG(LOG_LEVEL_INFO, "inserted item %d at back\n", list.back());

    string ans;
    for (int num : list.list()) {
        ans += to_string(num) + " ";
    }
    LOG(LOG_LEVEL_INFO, "linked list : %s\n", ans.c_str());
    return 0;
}