#include "logger.h"
#include <vector>
#include <unordered_map>

using namespace std;

class Cache {
    public:
        Cache(int lines);
        int Fetch(int process);
        int Least_recently_used();

    private:
        int i = 0;
        vector<int> age_bits;
        vector<vector<int>> cache;
        unordered_map<int, int> process_index;

        void Fill(int process);
        void Replace(int process);
        int Search(int process);
        void Get_age_bits();
        void Get_cache_lines();
};