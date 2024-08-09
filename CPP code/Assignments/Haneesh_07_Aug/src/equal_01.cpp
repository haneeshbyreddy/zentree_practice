#include "logger.h"
#include <string>

using namespace std;

int main() {
    string input_string = "0100110101";
    LOG(LOG_LEVEL_INFO, "Input binary : %s", input_string.c_str());

    int count = 0;
    int ans = 0;
    for (char i : input_string){
        if (i == '0') count++;
        else count--;
        if (count == 0) ans++;
    }
    LOG(LOG_LEVEL_INFO, "Equal collection of 0's and 1's are %d\n", ans);
}