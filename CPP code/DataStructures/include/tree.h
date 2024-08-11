#include "logger.h"

class Tree {
    struct TreeNode {
        int val;
        TreeNode* left = nullptr;
        TreeNode* right = nullptr;
    };

    Tree(int val);

    void addNode(int val);
};