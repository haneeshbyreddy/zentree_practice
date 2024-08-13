#include "hash.h"

int main() {
    Hash dict1(10);
    for (int i : {2,3,4}) {
        dict1.insert(i, i+10);
    }
    dict1.insert(12, 35);
    LOG(LOG_LEVEL_INFO, "value of 2 : %d", dict1.get_value(2));
    LOG(LOG_LEVEL_INFO, "value of 12 : %d", dict1.get_value(12));
}