#ifndef GRAPH_H
#define GRAPH_H

#include "logger.h"
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

class Graph {
public:
    Graph(int size);

    void add_node();
    void delete_node();
    void insert_link(int i, int j, int weight = 1);
    void delete_link(int i, int j);

    string print_matrix();
    unordered_set<int> BFT(int node);
    unordered_set<int> DFT(int node);
    int shortest_path(int i, int j);

private:
    vector<std::vector<int>> matrix;
    unordered_set<int> dft_set;
    unordered_set<int> shortest_path_s;
    int shortest_distance;

    vector<std::vector<int>> get_matrix(int size);
    int shortest_path_helper(int i, int j, int d);
};

#endif