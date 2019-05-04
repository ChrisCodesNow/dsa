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

void Queue :: pop(){
  if(size() > 0){
    //up to size() - 1, to avoid accessing out of bound array by Q[i + 1]
    for(int i = 0; i < size() - 1; i++){
      Q[i] = Q[i + 1];
    }
    count -= 1;
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
