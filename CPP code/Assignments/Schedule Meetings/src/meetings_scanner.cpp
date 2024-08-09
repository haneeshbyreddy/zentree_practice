#include "meetings_scanner.h"

unordered_map<int, int> max_meetings_dict;
vector<int> start_times_local;
vector<int> end_times_local;

int GetValues(vector<int> start_times, vector<int> end_times) {
    start_times_local = start_times;
    end_times_local = end_times;
    return 1;
}
int Scan(int i) {
    LOG(LOG_LEVEL_DEBUG, "Scanning with meeting at index %d", i);
    if (max_meetings_dict.find(i) != max_meetings_dict.end()) {
        return max_meetings_dict[i];
    }
    int maximum_meetings = 1;
    for (int j = 0; j < start_times_local.size(); j++) {
        if (start_times_local[j] > end_times_local[i]) {
            maximum_meetings = max(maximum_meetings, 1 + Scan(j));
        }
    }
    max_meetings_dict[i] = maximum_meetings;
    LOG(LOG_LEVEL_DEBUG, "Possible meetings with index %d is %d", i, maximum_meetings);
    return maximum_meetings;
}