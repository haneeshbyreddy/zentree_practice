#include "logger.h"
#include <vector>

using namespace std;

int main() {
    int length = 6;
    int input_arr[] = {16,17,4,3,5,2};
    int major = input_arr[length-1];
    vector<int> ans;

    for (int i=length-1;i>=0;i--) {
        if (input_arr[i] >= major) {
            ans.push_back(input_arr[i]);
            major = input_arr[i];
        }
    }

    for (int i : ans) {
        LOG(LOG_LEVEL_INFO, "Array leaders are %d", i);
    }
}