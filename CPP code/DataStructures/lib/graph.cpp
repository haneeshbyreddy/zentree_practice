#include "graph.h"

Graph::Graph(int size) {
    matrix = get_matrix(size);
}

string Graph::print_matrix() {
    string temp = "";
    for (auto node : matrix) {
        for (int connection : node) {
            temp += (to_string(connection) + " ");
        }
        temp += "\n";
    }
    return temp;
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

void Graph::insert_link(int i, int j) {
    matrix[i][j] = 1;
    matrix[j][i] = 1;
}

void Graph::delete_link(int i, int j) {
    matrix[i][j] = 0;
    matrix[j][i] = 0;
}

unordered_set<int> Graph::BFT(int node) {
    vector<int> my_queue;
    unordered_set<int> bft_set;

    my_queue.push_back(node);

    while (my_queue.size() > 0) {
        int i = my_queue.front();
        my_queue.erase(my_queue.begin());
        bft_set.insert(i);

        for (int j=0; j<matrix[0].size(); j++) {
            if (matrix[i][j] == 1 && bft_set.find(j) == bft_set.end()) {
                my_queue.push_back(j);
            }
        }
    }
    return bft_set;
}

unordered_set<int> Graph::DFT(int node) {
    dft_set.insert(node);

    for (int i=0; i<matrix[0].size(); i++) {
        if (matrix[node][i] == 1 && dft_set.find(i) == dft_set.end()) {
            Graph::DFT(i);
        }
    }
    return dft_set;
}