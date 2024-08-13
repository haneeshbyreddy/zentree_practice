#include "hash.h"
#include <stdexcept>

Hash::Hash(int val) {
    HASH_SIZE = val;
    for (int i=0;i<val;i++) {
        arr.push_back(list<pair<int, int>>());
    }
}

void Hash::insert(int val1, int val2) {
    int mod_key = val1 % HASH_SIZE;
    for (auto li = arr[mod_key].begin(); li != arr[mod_key].end(); li++) {
        if (li->first == val1) {
            throw std::runtime_error("key already exist");
        }
    }
    arr[mod_key].push_back(make_pair(val1, val2));
    keys++;
}

int Hash::get_value(int val) {
    int mod_key = val % HASH_SIZE;
    for (auto li = arr[mod_key].begin(); li != arr[mod_key].end(); li++) {
        if (li->first == val) {
            return li->second;
        }
    }
    return -1;
}