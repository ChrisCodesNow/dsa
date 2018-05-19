
#ifndef STACK_H
#define STACK_H
#include <string>
using namespace std;

class Stack{
public:
  //constructor
  Stack();
  //Insert x to stack
  void push(string x);
  //remove top item from stack
  void pop();
  //get top item from stack
  string top();
  //get size of the stack
  int size();
private:
  int count;      //counts number of elements in the stack
  int capacity;   //max number of elements allowed
  string S[1000];
};


#endif
