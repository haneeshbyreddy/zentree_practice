#include "logger.h"
#include <string>

using namespace std;

int main() {
    string word_1 = "mightandmagic";
    string word_2 = "andmagicmight";
    LOG(LOG_LEVEL_INFO,"Given word1 : %s, word2 : %s", word_1.c_str(), word_2.c_str());

    int ans = -1;
    int n = word_1.size();

    for(int i=0;i<n;i++) {
        if (word_1 == word_2) {
            ans = i;
            break;
        }
        char temp = word_2[n-1];
        for (int j=n-2;j>=0;j--) {
            word_2[j+1] = word_2[j];
        }
        word_2[0] = temp;
    }
    LOG(LOG_LEVEL_INFO,"Rotation count is %d\n", ans);
    return 0;
}