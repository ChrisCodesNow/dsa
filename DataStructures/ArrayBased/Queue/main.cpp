#include <iostream>
using namespace std;
#include "queue.h"

int main() {
  cout << "hello world" << endl;

  Queue Q;
  Q.push("air");
  Q.push("boat");
  Q.push("cattle");
  Q.push("dog");
  Q.push("elephant");
  Q.push("fire");
  Q.push("gallon");
  Q.push("house");
  Q.push("iron");

  while (Q.size() > 0){
    cout << "Removing " << Q.front() << endl;
    Q.pop();
  }
  Q.push("Zip");
  cout << "Removing " << Q.front() << endl;
  Q.pop();
}
