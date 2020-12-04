#include <iostream>
using namespace std;

struct rootNode{
    int key;
    rootNode *left;
    rootNode *right;
    rootNode(int k) {
        key = k;
        left=right=NULL;
    }
};

int main() {
    rootNode *root = new rootNode(10);
    root -> left = new rootNode(20);
    root -> right = new rootNode(30);
    root -> left -> left = new rootNode(40);
    cout<<root->right->key<<endl;
    return 0;
}