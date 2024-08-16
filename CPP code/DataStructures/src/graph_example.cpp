#include "graph.h"
#include <string>

using namespace std;

int main() {
    Graph my_graph(5);

    my_graph.insert_link(0,1);
    my_graph.insert_link(1,2);
    my_graph.insert_link(0,3);
    my_graph.insert_link(3,4);
    my_graph.insert_link(2,4);

    my_graph.add_node();
    my_graph.insert_link(2,5);

    LOG(LOG_LEVEL_INFO, "Adjacency Matrix: \n%s", my_graph.print_matrix().c_str());

    auto bft_arr = my_graph.BFT(0);
    string nodes_bft = "";
    for (int i : bft_arr) {
        nodes_bft += (to_string(i) + " ");
    }
    LOG(LOG_LEVEL_INFO, "BFT nodes : %s\n", nodes_bft.c_str());


    auto dft_arr = my_graph.DFT(0);
    string nodes_dft = "";
    for (int i : dft_arr) {
        nodes_dft += (to_string(i) + " ");
    }
    LOG(LOG_LEVEL_INFO, "BFT nodes : %s\n", nodes_dft.c_str());

    int i = 0, j = 4;
    LOG(LOG_LEVEL_INFO, "shortest path %d, %d : %d", i, j, my_graph.shortest_path(i,j));
    // my_graph.shortest_path(i, j);
    return 0;
}