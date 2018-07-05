#include "bst.h"

BST :: BST (){
	root = nullptr;
	count = 0;
}

bool BST :: empty(){
	return root == nullptr;
}
Node* BST :: find(string x){
	return find_recurse(x, root);
}

void BST :: insert(string x){
	// case 1: Emtpy tree, insert at root.
	// case 2: Insert into sorted position in left or right subtree
	if(root == nullptr){
		root = new Node(x);
		count += 1;
	}
	else{
		// Insert or keep iterating
		Node* itr = root;
		while(itr != nullptr){
			if(x < itr->data && itr->left == nullptr){
				itr->left = new Node(x);
				count += 1;
				break;
			}
			else if(x > itr->data && itr->right == nullptr){
				itr->right = new Node(x);
				count += 1;
				break;
			}

			if(x < itr->data){
				itr = itr->left;
			}
			else{
				itr = itr->right;
			}
		}
	}
}

void BST :: make_empty(){
	while(!empty()){
		cout << "removing: " << root->data << endl;
		remove(root->data);
	}
}
void BST :: remove(string x){

	// Find doomed node
	Node* doomed = find(x);

	// Erase doomed, if it is on tree
	// Find the parent and handle one of 3 cases
	// Case 1: doomed is a leaf
	// Case 2: doomed is internal node
	// Case 3: doomed has 2 children

	if(has_node(doomed)){
		Node* parent_of_doomed = find_parent(doomed);

		if (has_two_children(doomed)){
			remove_node_two_children(doomed, parent_of_doomed);
		}
		else if(has_one_child(doomed)){
			remove_node_one_child(doomed, parent_of_doomed);
		}
		else
		{
			remove_leaf(doomed, parent_of_doomed);
		}
		count -= 1;
	}
}

void BST :: print(){
	cout << "BST size: " << count << endl;
	print_recurse(this->root);
}

int BST :: size(){
	return count;
}



// //////////////////////////////////////////////
// //////////////////////////////////////////////
// Helper methods



Node* BST :: find_min(Node* node_itr){
	while(node_itr->left != nullptr){
		node_itr = node_itr->left;
	}

	return node_itr;
}

Node*  BST :: find_parent(Node* child){
	if(child == root){
		return nullptr;
	}
	else{
		return find_parent_recurse(child, root);
	}
}

Node* BST :: find_recurse(string x, Node* root){
	if(root == nullptr){
		return nullptr;
	}
	else if(x == root->data){
		return root;
	}
	else if(x < root->data){
		return find_recurse(x, root->left);
	}
	else{
		return find_recurse(x, root->right);
	}
}

Node* BST :: find_parent_recurse(Node* child, Node* node_itr){
	if(node_itr->is_parent_of(child)){
		return node_itr;
	}
	else if(child->data < node_itr->data){
		return find_parent_recurse(child, node_itr->left);
	}
	else{
		return find_parent_recurse(child, node_itr->right);
	}
}

bool BST :: has_node(Node* node){
	return node != nullptr;
}


bool BST :: has_two_children(Node* node){
	return node->left != nullptr && node->right != nullptr;
}

bool BST :: has_one_child(Node* node){
	return node->left != nullptr || node->right != nullptr;
}

bool BST :: is_leaf(Node* node){
	return node->left == nullptr && node->right == nullptr;
}

void BST :: print_recurse(Node* root){
	if(root == nullptr){
		return;
	}
	else{
		print_recurse(root->left);
		cout << root->data << endl;
		print_recurse(root->right);
	}
}

void BST :: remove_leaf(Node* &leaf, Node* &parent){
	// Update parent_of_doomed child, if parent exists
	// Delete doomed

	if(has_node(parent)){
		if(parent->left == leaf){
			parent->left = nullptr;
		}
		else{
			parent->right = nullptr;
		}
	}
	else{
		root = nullptr;
	}
	delete leaf;
}

void BST :: remove_node_one_child(Node* &node, Node* &parent){
	// Determine if node has a left or right child
	// 	Case 1: node is an internal node
	// 	Case 2: node is the root
	// Delete the node

	if(node->left != nullptr){
		if(has_node(parent)){
			parent->left = node->left;
		}
		else{
			root = node->left;
		}
	}
	else{
		if(has_node(parent)){
			parent->right = node->right;
		}
		else{
			root = node->right;
		}

	}
	delete node;
}

void BST :: remove_node_two_children(Node* &node, Node* &parent){

	// Find next largest node = smallest on the right
	// Swap contents of node and next_min
	// Erase next_min, now contains the data of the node to be deleted
	
	Node* next_min = find_min(node->right);
	Node* parent_of_next_min = find_parent(next_min);

	swap(node->data, next_min->data);

	if(has_one_child(doomed)){
		remove_node_one_child(next_min, parent_of_next_min);
	}
	else{
		remove_leaf(next_min, parent_of_next_min);
	}
}




