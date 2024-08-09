#include "heap.h"

using namespace std;

vector<int> Heap::Heapify(vector<int> arr) {
    int left, right, temp, high;

    for(int i=(arr.size()/2)-1;i>=0;i--) {
        left = 2*i + 1, right = 2*i + 2;

        while ((right<arr.size() || left<arr.size()) && (arr[right] > arr[i] || arr[left] > arr[i])) {
            if (arr[right] < arr[left]) high = left;
            else high = right;
            swap(arr[high], arr[i]);
            i = high;
            left = 2*i + 1, right = 2*i + 2;
        };
    }
    return arr;
}
