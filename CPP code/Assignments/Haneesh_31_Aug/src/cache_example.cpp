#include "cache.h"
#include <iostream>

int main() {
    int lines;
    std::cout << "Enter the number of lines in the cache: ";
    std::cin >> lines;

    Cache p_lru(lines);
    int value;

    std::cout << "Enter values to insert into the cache (enter -1 to stop):\n";
    while (std::cin >> value && value != -1) {
        p_lru.Fetch(value);
    }

    return 0;
}
