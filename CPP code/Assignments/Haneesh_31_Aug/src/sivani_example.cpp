#include <iostream>
#include <algorithm> 

using namespace std;

class PseudoLRU 
{
    public:
        PseudoLRU() 
        {
            b0 = false;
            b1 = false;
            b2 = false;
            for (int i = 0; i < 4; ++i) 
            {
                cache[i] = -1;
            }
        }

        int getLRU()  
        {
            if (!b0 && !b1) 
            {
                return 0;
            } 
            else if (!b0 && b1) 
            {
                return 1;
            } 
            else if (b0 && !b2) 
            {
                return 2;
            } 
            else 
            {
                return 3;
            }
        }

        void update(int processedIndex) 
        {
            switch (processedIndex) 
            {
                case 0: b0 = true; 
                    break;  
                case 1: b1 = true; 
                    b0 = false;
                    break;
                case 2: b2 = true; 
                    b0 = true; 
                    break; 
                case 3: b2 = false;
                    b0 = true; 
                    break; 
            }
        }

        void process(int address) 
        {
            int lruIndex = getLRU();

            if (find(begin(cache), end(cache), address) != end(cache)) 
            {
                cout << "Address " << address << " is already in cache.\n";
            } 
            else 
            {
                cout << "Replacing cache block " << lruIndex << " with address " << address << ".\n";
                cache[lruIndex] = address;
                update(lruIndex);
            }

            cout << "Current cache: ";
            for (int i : cache) {
                cout << i << " ";
            }
            cout << "\n";
        }

    private:
        int cache[4];  
        bool b0, b1, b2;  
};

int main() 
{
    PseudoLRU plru;


    int processSequence[] = {0, 1, 2, 3, 1, 2, 0, 3, 4};

    for (int address : processSequence) 
    {
        plru.process(address);
    }

    return 0;
}