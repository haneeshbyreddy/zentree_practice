#include "graph.h"

Graph::Graph(int size) {
    matrix = get_matrix(size);
}

vector<vector<int>> Graph::get_matrix(int size) {
    vector<vector<int>> temp;
    for (int i=0;i<size;i++) {
        temp.push_back(vector<int>());
        for (int j=0;j<size;j++) {
            temp[i].push_back(0);
        }
    }
    return temp;
}

void Graph::insert(int i, int j) {
    matrix[i][j] = 1;
    matrix[j][i] = 1;
}

