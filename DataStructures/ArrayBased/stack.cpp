#include "stack.h"

Stack :: Stack(){
  count = 0;
}

void Stack :: push(string x){
  if(count < capacity){
    S[count] = x;
    count += 1;
  }
  else{
    abort();
  }
  
}

void Stack :: pop(){
  //Only remove when stack has items.
  if(size() > 0){
    count -= 1;
  }
}

int Stack :: size(){
  return count;
}
