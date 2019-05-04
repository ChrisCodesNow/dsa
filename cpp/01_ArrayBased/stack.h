
#ifndef STACK_H
#define STACK_H
#include <string>
using namespace std;

class Stack{
public:
  //constructor
  //O(1)
  Stack();
  
  //Insert x to stack
  //O(1)
  void push(string x);
  
  //remove top item from stack
  //O(n), need to shift remaining items to the front of the Queue.
  void pop();
  
  //get top item from stack
  //O(1)
  string top();
  
  //get size of the stack
  //O(1)
  int size();
private:
  int count;      //counts number of elements in the stack
  int capacity;   //max number of elements allowed
  string S[1000];
};


#endif
