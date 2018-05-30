
#include <chrono>
#include <string>
#include <iostream>
#include "stack.h"

using namespace std;
using namespace chrono;

inline void _test(const char* expression, const char* file, int line)
{
	cerr << "test(" << expression << ") failed in file " << file;
	cerr << ", line " << line << "." << endl;
	abort();
}
#define test(EXPRESSION) ((EXPRESSION) ? (void)0 : _test(#EXPRESSION, __FILE__, __LINE__))


int main() 
{
	Stack s; // []
	test(s.size() == 0);

	s.push("hello"); // ["hello"]
	test(s.top() == "hello");
	test(s.size() == 1);

	s.push("dog"); // ["hello", "dog"]
	test(s.size() == 2);
	test(s.top() == "dog");

	s.push("phone"); // ["hello", "dog", "phone"]
	test(s.size() == 3);
	test(s.top() == "phone");

	s.pop(); // ["hello", "dog"]
	test(s.size() == 2);
	test(s.top() == "dog");
	
	s.push("cat"); // ["hello", "dog", "cat"]
	test(s.size() == 3);
	test(s.top() == "cat");

	s.pop(); // ["hello", "dog"]
	test(s.size() == 2);
	test(s.top() == "dog");

	s.pop(); // ["hello"]
	test(s.size() == 1);
	test(s.top() == "hello");

	s.pop(); // []
	test(s.size() == 0);

	int large = 10000000;
	for (int i = 0; i < large; ++i)
	{
		test(s.size() == 0);
		s.pop();
		s.top();
	}

	cout << "Passed basic tests." << endl;


	// Test many pushes
	for (int i = 0; i < large; ++i)
		s.push("dog");
	test(s.size() == large);
	test(s.top() == "dog");
	s.pop();
	test(s.top() == "dog");

	cout << "Passed pushing " << large << " items." << endl;

	for (int l = 10000; l <= 10000000; l += 10000)
	{
		system_clock::time_point start = system_clock::now();
		Stack s;
		for (int i = 0; i < l; ++i)
			s.push("dog");	
		system_clock::time_point end = system_clock::now();
	        float elapsed_time = duration<float>(end-start).count();
		cout << l << "	" << elapsed_time << endl;
		//cout << "Elapsed time was " << elapsed_time << " seconds." << endl;
	}
}



