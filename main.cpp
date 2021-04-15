#include<bits/stdc++.h>

#include <math.h>

using namespace std;

/*  Tree node structure */
struct Node {
  int key;
  struct Node * left, * right;
};

// Returns depth of leftmost leaf.
int findADepth(Node * node) {
  int d = 0;
  while (node != NULL) {
    d++;
    node = node -> left;
  }
  return d;
}

bool isPerfectRec(struct Node * root, int d, int level = 0) {

  if (root == NULL)
    return true;

  if (root -> left == NULL && root -> right == NULL)
    return (d == level + 1);

  if (root -> left == NULL || root -> right == NULL)
    return false;

  return isPerfectRec(root -> left, d, level + 1) &&
    isPerfectRec(root -> right, d, level + 1);
}

bool isPerfect(Node * root) {
  int d = findADepth(root);
  return isPerfectRec(root, d);
}

struct Node * newNode(int k) {
  struct Node * node = new Node;
  node -> key = k;
  node -> right = node -> left = NULL;
  return node;
}

Node * insertLevelOrder(int arr[], Node * root,
  int i, int n) {
  if (i < n) {
    Node * temp = newNode(arr[i]);
    root = temp;

    root -> left = insertLevelOrder(arr,
      root -> left, 2 * i + 1, n);

    root -> right = insertLevelOrder(arr,
      root -> right, 2 * i + 2, n);
  }
  return root;
}

void storeBSTNodes(Node * root, vector < Node * > & nodes) {

  if (root == NULL)
    return;

  storeBSTNodes(root -> left, nodes);
  nodes.push_back(root);
  storeBSTNodes(root -> right, nodes);
}

Node * buildTreeUtil(vector < Node * > & nodes, int start,
  int end) {

  if (start > end)
    return NULL;

  int mid = (start + end) / 2;
  Node * root = nodes[mid];

  root -> left = buildTreeUtil(nodes, start, mid - 1);
  root -> right = buildTreeUtil(nodes, mid + 1, end);

  return root;
}

Node * buildTree(Node * root) {

  vector < Node * > nodes;
  storeBSTNodes(root, nodes);

  int n = nodes.size();
  return buildTreeUtil(nodes, 0, n - 1);
}

void preOrder(Node * node) {
  if (node == NULL)
    return;
  cout << node -> key << " ";
  preOrder(node -> left);
  preOrder(node -> right);
}

void inOrder(Node * root) {
  if (root != NULL) {
    inOrder(root -> left);
    cout << root -> key << " ";
    inOrder(root -> right);
  }
}

Node * InitTree(Node * root) {
  int h = 0;
  cout << "Enter height of tree: ";
  cin >> h;

  int n = pow(2, h) - 1;
  cout << "Number of nodes = " << n << endl;
  int arr[n] = {};

  for (int i = 0; i < n; ++i) {
    cout << "Enter node #" << i << ": ";
    cin >> arr[i];
  }

  root = insertLevelOrder(arr, root, 0, n);

  return root;
}

int main() {
  struct Node * root = NULL;
  root = InitTree(root);

  cout << endl << "Your tree:" << endl;
  preOrder(root);
  cout << endl;
  if (isPerfect(root))
    cout << "The tree is a perfect binary tree\n";
  else
    cout << "The tree is not a perfect binary tree\n";

  root = buildTree(root);

  cout << endl << "Balanced tree:" << endl;
  preOrder(root);

  return (0);
}