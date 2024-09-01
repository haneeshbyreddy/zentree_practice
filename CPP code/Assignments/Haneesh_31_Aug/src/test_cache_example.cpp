#include "cache.h"
#include <cassert>

void testPseudoLRU() {
    Cache p_lru1(4);

    p_lru1.Fetch(1);
    p_lru1.Fetch(2);
    p_lru1.Fetch(3);
    p_lru1.Fetch(4);
    assert(p_lru1.Least_recently_used() == 1); 

// 0, 1, 2, 3, 1, 2, 0, 3, 4

    Cache p_lru2(10);

    p_lru2.Fetch(0);
    p_lru2.Fetch(1);
    p_lru2.Fetch(2);
    p_lru2.Fetch(3);
    p_lru2.Fetch(1);
    p_lru2.Fetch(2);
    p_lru2.Fetch(0);
    p_lru2.Fetch(3);
    p_lru2.Fetch(4);

    assert(p_lru2.Least_recently_used() == 1); 

}

int main() {
    testPseudoLRU();
    return 0;
}