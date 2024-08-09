#include "logger.h"
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    string arr[] = {"john","johnny","jackie","johnny","john","jackie","jamie","jamie","john","johnny","jamie","johnny","john"};

    int maxi = 0;
    unordered_map<string, int> dict;
    string ans = "~";

    for (string name : arr) {
        if (dict.find(name) == dict.end()) dict[name] = 1;
        else dict[name]++;
        if (dict[name] > maxi) maxi = dict[name];
    }
    for (auto name : dict) {
        if (name.second == maxi) {
            if (name.first < ans) {
                ans = name.first;
            }
        }
    }
    LOG(LOG_LEVEL_INFO, "%s won with %d votes\n", ans.c_str(), maxi);
}