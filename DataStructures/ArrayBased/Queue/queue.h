#ifndef QUEUE_H
#define QUEUE_H

#include <string>
using namespace std;

class Queue{
public:
  //Default constructor
  Queue();
  //insert new element to back of Queue
  void push(string x);
  //remove front element from Queue
  void pop();
  //get, but do not remove, front element from Queue
  string front();
  //get number of elements in the Queue
  int size();

private:
  int count;  //Count current number of elements in Queue
  int capacity; //Maximum number allowed of elements in Queue
  string Q[1000];   //Stack for 1,000 elements
};

#endif
