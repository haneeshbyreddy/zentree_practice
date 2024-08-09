#ifndef HEAP_H
#define HEAP_H

#include <vector>
#include "logger.h"

class Heap {
public:
    static std::vector<int> Heapify(std::vector<int> arr);
};

#endif