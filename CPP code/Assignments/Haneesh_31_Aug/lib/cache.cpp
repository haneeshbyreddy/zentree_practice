#include "cache.h"
#include <iostream>

using namespace std;

Cache::Cache(int lines) {
    cache.resize(lines, vector<int>(1));
    for (int j=1;j<lines;j++) age_bits.push_back(0);
};

void Cache::Get_age_bits() {
    for (int i : age_bits) cout << i << " ";
    cout << "\n";
}

void Cache::Get_cache_lines() {
    string ans = "";
    for (vector<int> i : cache) cout << i[0] << " ";
    cout << "\n\n";
}

int Cache::Least_recently_used() {
    i = 0;
    while((2*i)+1<age_bits.size()) {
        i = (age_bits[i] == 0) ? (2*i)+2 : (2*i)+1;
    }
    int index = (i - (age_bits.size()/2))*2 + (age_bits[i]*-1)+1;
    return cache[index][0];
}

int Cache::Search(int process) {
    int i = 0;
    float adjust = cache.size()/2;
    float curr = cache.size()/2 - 0.5;

    while(i<age_bits.size()) {
        if (curr > process_index[process]) {
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
    return process;
}

void Cache::Replace(int process) {
    i = 0;
    while((2*i)+1<age_bits.size()) {
        age_bits[i] = (age_bits[i] * -1) + 1;
        i = (age_bits[i] == 0) ? (2*i)+1 : (2*i)+2;
    }
    age_bits[i] = (age_bits[i] * -1) + 1;

    int index = (i - (age_bits.size()/2))*2 + age_bits[i];
    cache[index][0] = process;
    process_index[process] = index;
}

int Cache::Fetch(int process) {
    if (process_index.find(process) == process_index.end()) Replace(process);
    else Search(process);

    Get_age_bits();
    Get_cache_lines();
    return process;
}