#include "logger.h"
#include <cstdint>
#include <vector>

using namespace std;

class Cache {
    public:
        Cache(int size, int lines, int blocks);
    private:
        vector<vector<uint8_t>> cache;
        vector<vector<uint8_t>> blocks;
        vector<int> age_bits;
};