#include "cache.h"
#include <iostream>
#include <cassert>

void testPseudoLRU() {
    Cache p_lru1(4);

    p_lru1.Fetch(1);
    p_lru1.Fetch(2);
    p_lru1.Fetch(3);
    p_lru1.Fetch(4);
    assert(p_lru1.Least_recently_used() == 1); 
}

int main() {
    testPseudoLRU();
    return 0;
}