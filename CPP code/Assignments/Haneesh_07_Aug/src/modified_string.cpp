#include "logger.h"
#include <string>

using namespace std;

int main() {
    string letters = "aabbbcccdddddd";
    LOG(LOG_LEVEL_INFO, "Given letters are : %s", letters.c_str());

    int val = 0, ans = 0;

    for (char c : letters) {
        int c_num = (int)c;

        if (val % c_num == 0) val += c_num;
        else val = c_num;

        if (val == (c_num * 3)) {
            ans += 1;
            val = c_num;
        }
    }
    LOG(LOG_LEVEL_INFO, "minimum number of characters required are %d\n", ans);
}