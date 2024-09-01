#include "cache.h"
#include <iostream>
#include <string>

using namespace std;

int main() {
    int lines;
    cout << "Enter the number of lines in the cache: ";
    cin >> lines;
    Cache p_lru(lines);

    string input;
    cout << "Enter 'f <number>' to fetch a process, 'r' to get recently used :\n";

    while (cin >> input && input != "q") {
        if (input == "f") {
            int process;
            cin >> process;
            p_lru.Fetch(process);
        } else if (input == "r") {
            int recent = p_lru.Least_recently_used();
            cout << "Least Recently used: " << recent << endl;
        } else {
            cout << "Invalid input. Use 'f <number>', 'r', or 'q'.\n";
        }
    }

    return 0;
}