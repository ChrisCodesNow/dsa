#include "queue.h"

Queue :: Queue(){
  count = 0;
  capacity = 1000;
}

void Queue :: push(string x){
  if(size() < capacity){
    Q[count] = x;
    count += 1;
  }
  else{
    abort();
  }
}

string Queue :: front(){
  if(size() > 0){
    return Q[count - 1];
  }
  else{
    abort();
  }
}
int Queue :: size(){
  return count;
}
