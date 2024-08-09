#include "logger.h"
#include <vector>

using namespace std;

class Stack {

	public:
		void PushItem(int var) {
			arr.push_back(var);
		};
		int PopItem() {
			int popped = arr.back();
			arr.pop_back();
			return popped;
		}
		int TopItem() {
			return arr.back();
		}
		bool IsEmpty() {
			return arr.size() == 0;
		};
	private:
		vector<int> arr;
};

int main() {
	Stack s1;
	for (int i : {1,4,2,5}) {
		s1.PushItem(i);
		LOG(LOG_LEVEL_INFO, "Pushed item %d", i);
	}
	LOG(LOG_LEVEL_INFO, "Popped item %d", s1.PopItem());
	LOG(LOG_LEVEL_INFO, "Top item %d", s1.TopItem());
	return 0;
}
