#include "logger.h"
#include <cstdint>
#include <vector>
#include <unordered_map>

using namespace std;

class Cache {
    public:
        Cache(int lines);
        int Fetch(int val);

    private:
        int i = 0;
        bool filled = false;
        vector<int> age_bits;
        vector<vector<int>> cache;
        unordered_map<int, int> val_index;

        void Fill(int val);
        void Replace(int val);
        int Search(int val);
        void get_age_bits();
};