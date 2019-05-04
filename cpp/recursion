#include <iostream>
using namespace std;
/*
fact(4) = 4 * fact(3)
fact(3) = 3 * fact(2)
fact(2) = 2 * fact(1)
fact(1) = 1
*/
//Recursively find factorial of n
int factorial(int n){
  if(n == 1|| n == 0){
    return 1;
  }
  else{
    return n * factorial(n -1);
  }
}
int main() {
  for(int i = 0; i < 10; i++){
    
    cout << i << "\t" << factorial(i) << endl;
  }
}
