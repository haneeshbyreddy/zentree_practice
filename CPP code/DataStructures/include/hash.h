#include "logger.h"
#include <list>
#include <vector>
#include <utility>

using namespace std;

class Hash {
    public:
        vector<list<pair<int, int>>> arr;
        int HASH_SIZE = 10;
        int keys = 0;

        Hash(int val);

        void insert(int val1, int val2);
        int get_value(int val);
};