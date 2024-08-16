#include "logger.h"
#include <vector>

using namespace std;

class Graph {
    public:
        vector<vector<int>> matrix;
        
        Graph(int size);

        vector<vector<int>> get_matrix(int size);
        void insert(int i, int j);
};