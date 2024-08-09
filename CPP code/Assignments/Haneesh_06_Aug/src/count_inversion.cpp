#include "logger.h"

int main() {
    int length = 5;
    int input_arr[] = {2, 4, 1, 3, 5};
    int count = 0;
    for (int i=0;i<length-1;i++) {
        for (int j=i+1;j<length;j++) {
            if (input_arr[i] > input_arr[j]) {
                count++;
            }
        }
    }
    LOG(LOG_LEVEL_INFO, "Inversion Count %d", count);
}