#include "cache.h"

Cache::Cache(int size, int lines, int blocks_lines) {
    cache.resize(lines, vector<uint8_t>(size));
    blocks.resize(blocks_lines, vector<uint8_t>(size));
    for (int i=0;i<lines;i++) {
        age_bits.push_back(0);
    }
};

