#include "double_linked_list.h"
#include <string>

using namespace std;

int main() {
    DoubleLinked list;
    for (int i : {1,2,4,5,6}) {
        list.push_back(i);
    LOG(LOG_LEVEL_INFO, "pushed item %d", i);
    }
    LOG(LOG_LEVEL_INFO, "last elment %d", list.back());

    string ans;
    for (int num : list.list()) {
        ans += to_string(num) + " ";
    }
    LOG(LOG_LEVEL_INFO, "double linked list : %s\n", ans.c_str());
}
