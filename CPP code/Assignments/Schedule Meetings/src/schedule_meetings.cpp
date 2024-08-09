#include "logger.h"
#include "meetings_scanner.h"
using namespace std;

vector<int> start_times = {1, 3, 0, 5, 8, 5};
vector<int> end_times = {2, 4, 6, 7, 9, 9};


int main() {
    start_times.insert(start_times.begin(), -1);
    end_times.insert(end_times.begin(), -1);
    GetValues(start_times, end_times);
    int result = Scan(0) - 1;
    LOG(LOG_LEVEL_INFO, "Possible Mettings for given timings : %d", result);
    return 0;
}