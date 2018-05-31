#ifndef STACK_H
#define STACK_H

#include <string>
using namespace std;

class Stack{

	public:
		// Constructor
		Stack();

		// Destructor
		~Stack();

		// push new string to stack
		void push(string s);

		// Remove top item from stack
		void pop();

		// get top item from the stack.
		string top();


		// Get size of stack
		int size();
	private:
		string* A;		// Storage for stack
		int count;
		int capacity;		// Maximum data elements allowed before resizing

		// HELPER METHODS
		// Determine if stack is full or empty
		bool is_full();
		bool is_empty();
		
		// Enlarge stack, update capacity
		string* resize(string* old_A, int old_cap, int new_cap);
};

#endif