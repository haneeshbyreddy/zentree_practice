#include "cache.h"
#include <iostream>

int main() {
    int lines;
    std::cout << "Enter the number of lines in the cache: ";
    std::cin >> lines;

    Cache p_lru(lines);
    int process;

    std::cout << "Enter process to insert into the cache (enter -1 to stop):\n";
    while (std::cin >> process && process != -1) {
        p_lru.Fetch(process);
    }
    return 0;
}
