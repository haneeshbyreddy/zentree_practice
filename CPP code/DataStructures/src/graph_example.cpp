#include "graph.h"
#include <string>

using namespace std;

int main() {
    Graph my_graph(5);
    my_graph.insert(1,2);
    my_graph.insert(3,4);
    my_graph.insert(2,4);

    string temp = "";
    for (auto node : my_graph.matrix) {
        for (int connection : node) {
            temp += (to_string(connection) + " ");
        }
        temp += "\n";
    }
    LOG(LOG_LEVEL_INFO, "Adjacency Matrix: \n%s", temp.c_str());
    return 0;
}