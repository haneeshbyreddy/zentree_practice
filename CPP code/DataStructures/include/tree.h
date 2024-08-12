#include "logger.h"
#include <vector>

using namespace std;

struct BinaryNode {
    int value;
    BinaryNode* left = nullptr;
    BinaryNode* right = nullptr;

    BinaryNode(int value);
};

class BinaryTree {
    public:
        BinaryNode* root = nullptr;
        vector<BinaryNode*> q;

        BinaryTree(int val);

        void insert(int val);
        vector<int> BFT();
        vector<int> DFT();

    private:
        void dft(BinaryNode* node, vector<int>& ans);
        
};

class BinarySearchTree : public BinaryTree {
    public:
        void insert(int val);
        bool search(int val);
};