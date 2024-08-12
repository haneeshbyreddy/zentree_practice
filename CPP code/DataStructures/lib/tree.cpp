#include "tree.h"
#include <vector>

using namespace std;

BinaryNode::BinaryNode(int val) {
    value = val;
}

BinaryTree::BinaryTree(int val) {
    root = new BinaryNode(val);
    q.push_back(root);
};

void BinaryTree::insert(int val) {
    BinaryNode* temp = q.front();
    if (!temp->left) {
        temp->left = new BinaryNode(val);
        q.push_back(temp->left);
    } else {
        temp->right = new BinaryNode(val);
        q.push_back(temp->right);
    }

    if (temp->left && temp->right) {
        q.erase(q.begin());
    }
};

vector<int> BinaryTree::BFT() {
    vector<BinaryNode*> temp_q = { root };
    vector<int> ans;
    while (temp_q.size() > 0) {
        if (temp_q.front()->left) temp_q.push_back(temp_q.front()->left);
        if (temp_q.front()->right) temp_q.push_back(temp_q.front()->right);
        ans.push_back(temp_q.front()->value);
        temp_q.erase(temp_q.begin());
    }
    return ans;
};

void BinaryTree::dft(BinaryNode* node, vector<int>& ans) {
    if (node == nullptr) return;
    if (node->left) dft(node->left, ans);
    ans.push_back(node->value);
    if (node->right) dft(node->right, ans);
}

vector<int> BinaryTree::DFT() {
    vector<int> ans;
    dft(root, ans);
    return ans;
}

void BinarySearchTree::insert(int val) {
    BinaryNode* temp = root;
    while (temp->left && temp->value < val) {
        temp = temp->left;
    }
    while (temp->right && temp->value > val) {
        temp = temp->right;
    }
    if (temp->value < val) {
        temp->left = new BinaryNode(val);
    }
    else {
        temp->right = new BinaryNode(val);
    }
}