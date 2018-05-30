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


};

#endif