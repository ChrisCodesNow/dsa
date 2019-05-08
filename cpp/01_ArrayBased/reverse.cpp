#include <iostream>
#include <string>
using namespace std;

int main(){


    string word = "fire";
    int size = word.size();

    string reversed_word = "";

    for (int i = size - 1; i >= 0; i --){
        reversed_word =  reversed_word + word[i];
    }
    
    cout << reversed_word << endl;

    return 0;
}