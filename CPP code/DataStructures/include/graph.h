#include "logger.h"
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

class Graph {
    public:
        vector<vector<int>> matrix;
        unordered_set<int> dft_set;
        
        Graph(int size);

        vector<vector<int>> get_matrix(int size);
        void insert_link(int i, int j);
        void delete_link(int i, int j);

        string print_matrix();
        unordered_set<int> BFT(int node);
        unordered_set<int> DFT(int node);
};