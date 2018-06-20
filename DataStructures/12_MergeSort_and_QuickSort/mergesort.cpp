#include <iostream>

using namespace std;

void merge(int* A, int* left, int left_size, int* right, int right_size){
	// Create merged list
	int * sorted_A = new int[left_size + right_size];

	// Iterate through left and right lists
	// inserting the next smallest to the merged list
	int left_itr = 0;
	int right_itr = 0;
	int n = left_size + right_size;

	for(int itr = 0; itr < n; itr++){
		// Left and right have items remaining
		if(left_itr < left_size && right_itr < right_size){
			if(left[left_itr] < right[right_itr]){
				sorted_A[itr] = left[left_itr];
				left_itr += 1;
			}
			else{
				sorted_A[itr] = right[right_itr];
				right_itr += 1;
			}
		}
		// Only left has items remaining
		else if (left_itr < left_size){
			sorted_A[itr] = left[left_itr];
			left_itr += 1;
		}
		// Only right has items remaining
		else{
			sorted_A[itr] = right[right_itr];
			right_itr += 1;
		}
	}

	// Free up memory created in the merge routine
	for(int i = 0; i < n; i++){
		A[i] = sorted_A[i];
	}
	delete []sorted_A;
}

int* mergesort(int* A, int n){
	// Base case, list of size < 2 is already sorted.
	if(n < 2){
		return A;
	}

	// Recurively mergesort left and right halves
	int* left = mergesort(A, n/2);
	int* right = mergesort(&(A[n/2]), n - n/2);

	// Merge sorted left and right partions into A
	merge(A, left, n/2, right, n - n/2);

	return A;
}
