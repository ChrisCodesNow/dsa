
//Run time: O(n^2)
void quick_sort(int* A, int n){
	// Implied base case: List already sorted
	if(n < 2){
	
	}
	else{
		// Move items smaller than pivot left
		// Move items greater than pivot right
		// Place pivot in sorted position
		int pivot = n -1;	// Starting pivot position
		int separator = 0;	// Postion separating left and right subarrays
		for(int itr = 0; itr < n - 1; itr ++){
			if(A[itr] < A[pivot]){
				swap(A[itr], A[separator]);
				separator += 1;
			}
		}

		swap(A[pivot], A[separator]);

		// Recursively quick sort subarrays
		// to the left and right of the pivot
		quick_sort(A, separator);
		quick_sort(&(A[separator + 1]), n - separator - 1);
		
	}
}
