#include "stack.h"

Stack :: Stack(){
	count = 0;
	capacity = 10;
	
	A = new string[capacity];
}

Stack :: ~Stack(){}

void Stack :: push(string s){}

void Stack :: pop(){}

string Stack :: top(){}

int Stack :: size(){
	return count;
}

