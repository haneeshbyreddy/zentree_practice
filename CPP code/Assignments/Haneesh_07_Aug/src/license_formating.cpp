#include "logger.h"
#include <string>

using namespace std;

int main() {
    int k = 4;
    string license = "5F3Z-2e-9-w4";
    LOG(LOG_LEVEL_INFO, "license : %s, k : %d", license.c_str(), k);

    string ans = "";
    int length = 0;

    for (char c : license) {
        if (c != '-') {
            ans += c;
            length++;
        } 
    }
    for (int i=(length % k); i < length; i+=k) {
        if (i != 0) {
            ans.insert(i, "-");
            k++;
            length++;
        } 
    }
    LOG(LOG_LEVEL_INFO, "formated license is %s\n", ans.c_str());
}