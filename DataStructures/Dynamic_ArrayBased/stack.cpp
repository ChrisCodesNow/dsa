#include "stack.h"

Stack :: Stack(){
	count = 0;
	capacity = 10;
	
	A = new string[capacity];
}

Stack :: ~Stack(){}

void Stack :: push(string s){
	// Resize when needed
	if(is_full()){
		A = resize(A, capacity, capacity * 2);
	}

	// Add elements
	A[count] = s;
	count += 1;
}

void Stack :: pop(){
	if(!is_empty()){
		A[count - 1] = "";
		count -= 1;
	}
}

string Stack :: top(){
	if(!is_empty()){
		return A[count - 1];
	}
	else{
		return "";
	}
}

int Stack :: size(){
	return count;
}

// HELPER METHODS
bool Stack :: is_full(){
	return count == capacity;
}

bool Stack :: is_empty(){
	return count == 0;
}

string* Stack :: resize(string* old_A, int old_cap, int new_cap){
	string* new_A = new string[new_cap];

	// Copy existing items
	for(int i = 0; i < old_cap; i++){
		new_A[i] = old_A[i];	
	}

	delete[] old_A;
	capacity = new_cap;
	return new_A;
}

