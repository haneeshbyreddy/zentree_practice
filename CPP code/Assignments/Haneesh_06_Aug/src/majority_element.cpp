#include "logger.h"

using namespace std;

int main() {
    int input_arr[] = {1,2,4,2,1,6,1,2,2};
    int element = 0;
    int count = 0;
    for (int i : input_arr) {
        if (element != i) {
            if (count == 0) element = i;
            else count--;
        }
        else count++;
    }
    LOG(LOG_LEVEL_INFO, "Major Element is %d", element);
}