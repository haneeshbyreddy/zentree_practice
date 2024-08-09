#include "heap.h"
#include <string>
using namespace std;

int main() {
    vector<int> heapified_arr, arr = {3, 5, 8, 10, 17, 11, 13, 19, 22, 24, 29};
    heapified_arr = Heap::Heapify(arr);
    string ans, input_arr;
    for (int num : arr) {
        input_arr += to_string(num) + " ";
    }
    for (int num : heapified_arr) {
        ans += to_string(num) + " ";
    }
    LOG(LOG_LEVEL_INFO, "input arr : %s \nheapified arr : %s\n", input_arr.c_str(), ans.c_str());
}