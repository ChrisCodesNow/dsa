#ifndef BST_H
#define BST_H

#include <iostream>
#include "node.h"

class BST{
	public:
		BST();

		// Determine if tree is empty
		bool empty();

		// Find node with data x in the BST
		// use helper method find_recurse(...)
		Node* find(string x);

		// Insert x into the BST
		void insert(string x);

		// Remove all nodes from tree
		void make_empty();

		// Remove node with data x from the BST, if it exists
		void remove(string x);

		int size();

		void print();
		
	private:
		Node* root;
		int count;

		// //////////////////////////////////////////////
		// //////////////////////////////////////////////
		// Helper methods


		// Find node with smallest value in the subtree rooted at r
		Node* find_min(Node* node_itr);

		// Recursively find x in the BST
		// Base case: 
		// 	1. root is nullptr, return nullptr
		// 	2. x is the data of root, return root
		// Recursion: 
		//	Binary search in left or right subtree, where appropriate
		Node* find_recurse(string x, Node* root);


		// Determines if tree has given node
		bool has_node(Node* node);

		// Determine if node has exactly 2 children
		// Definition: internal node has at least 1 children
		bool has_two_children(Node* node);

		// Determine if node has exactly 1 child
		bool has_one_child(Node* node);

		// Determine if node is a leaf
		// Definition: leaf is a node with no children
		bool is_leaf(Node* node);

		// Find parent node of child node
		// Assume child is an existing node in the BST
		// child node has no parent when it is the root, return nullptr
		Node* find_parent(Node* child);

		// Recursively find the parent of child
		// Base Case:
		// 	Find partent when child of node_itr is child
		// Recursion:
		//	Appropriately search left or right subtree for partent
		Node* find_parent_recurse(Node* child, Node* node_itr);

		// Recursively print in order
		void print_recurse(Node* root);



		// Remove given leaf from the tree
		// Adjust given parent of leaf
		void remove_leaf(Node* &leaf, Node* &parent);

		// Remove given internal node from the tree.
		// Given node has exactly 1 child
		// Adjust given parent of internal node, if existent
		void remove_node_one_child(Node* &node, Node* &parent);
		
		// Remove given internal node with 2 children from the tree
		// Adjust given parent of internal node
		void remove_node_two_children(Node* &node, Node* &parent);


};

#endif
