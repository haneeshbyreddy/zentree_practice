#include <set>
#include <vector>
#include "logger.h"

using namespace std;


int main() {
    set<int> duplicates;
    set<int> seen_values;

    int n = 7;
    int input_arr[] = {0,1,3,2,3,0,1};

    for (int i : input_arr) {
        if (seen_values.find(i) != seen_values.end()) {
            duplicates.insert(i);
        }
        else {
            seen_values.insert(i);
        }
    }

    if (duplicates.size() == 0) {
        duplicates.insert(-1);
    }

    for (int i : duplicates) {
        LOG(LOG_LEVEL_INFO, "Duplicate elements in ascending order : %d", i);
    }
}