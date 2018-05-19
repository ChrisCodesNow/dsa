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

int Stack :: size(){
  return count;
}
