#include "stack.h"

Stack :: Stack(){
  count = 0;
}

void Stack :: push(string x){
  S[count] = x;
  count += 1;
}

int Stack :: size(){
  return count;
}
