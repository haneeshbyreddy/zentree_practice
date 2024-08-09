#include "logger.h"

int main() {
    int length = 4;
    int input_arr[] = {1,2,3,4};
    int x = 3;
    for (int i=0;i<length;i++){
        if (input_arr[i] == x) {
            LOG(LOG_LEVEL_INFO, "First element x in arr is at index %d", i);
            break;
        }
    }
    return 0;
}