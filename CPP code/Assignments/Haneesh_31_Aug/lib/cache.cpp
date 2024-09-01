#include "cache.h"
#include <iostream>

using namespace std;

Cache::Cache(int lines) {
    cache.resize(lines, vector<int>(1));
    for (int j=1;j<lines;j++) {
        age_bits.push_back(0);
    }
};

void Cache::get_age_bits() {
    string ans = "";
    for (int i : age_bits) {
        cout << i;
        cout << " ";
    }
    cout << "\n";
}

int Cache::Search(int val) {
    int i = 0;
    float adjust = cache.size()/2;
    float curr = cache.size()/2 + 0.5;

    while(i<age_bits.size()) {
        if (curr > val_index[val]) {
            age_bits[i] = 0;
            i = 2*i + 1;
            curr = curr - adjust/2;
        }
        else {
            age_bits[i] = 1;
            i = 2*i + 2;
            curr = curr + adjust/2;
        }
        adjust /= 2;
    }
    return val;
}

void Cache::Fill(int val) {
    while((2*i)+1<age_bits.size()) {
        if (age_bits[i] == 0) i = 2*i + 1;
        else i = 2*i + 2;
    }

    int index = (i - (age_bits.size()/2))*2 + age_bits[i];
    cache[index][0] = val;
    val_index[val] = index;
    LOG(LOG_LEVEL_DEBUG, "val : %d, index : %d", val, index);

    // LOG(LOG_LEVEL_DEBUG, "Current i in nodes :%d", i);
    // LOG(LOG_LEVEL_DEBUG, "Filled index %d in cache",index);

    if (age_bits[i] != 0) {
        if (i==age_bits.size()-1) filled = true;
        while (!filled && age_bits[i] != 0) i = (i-1)/2;
    }
    age_bits[i] = 1;
}

void Cache::Replace(int val) {
    i = 0;
    while((2*i)+1<age_bits.size()) {
        age_bits[i] = (age_bits[i] * -1) + 1;
        if (age_bits[i] == 0) i = 2*i + 1;
        else i = 2*i + 2;
    }
    age_bits[i] = (age_bits[i] * -1) + 1;

    int index = (i - (age_bits.size()/2))*2 + age_bits[i];
    cache[index][0] = val;
    val_index[val] = index;
    LOG(LOG_LEVEL_DEBUG, "val : %d, index : %d", val, index);

    // LOG(LOG_LEVEL_DEBUG, "Current i in nodes :%d", i);
    // LOG(LOG_LEVEL_INFO, "Replaced index %d in cache", index);
}

int Cache::Fetch(int val) {
    if (val_index.find(val) == val_index.end()) {
        if (!filled) Fill(val);
        else Replace(val);
    }
    else {
        Search(val);
    }
    get_age_bits();
    return val;
}