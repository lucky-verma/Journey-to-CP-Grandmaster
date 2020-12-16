// C++ program to print the
// Maximum number by concatenating
// every element in rotation of array
#include <bits/stdc++.h>
using namespace std;

// Function to print the largest number
void printLargest(int a[], int n)
{

	// store the index of largest
	// left most digit of elements
	int max = -1;
	int ind = -1;

	// Iterate for all numbers
	for (int i = 0; i < n; i++) {

		int num = a[i];

		// check for the last digit
		while (num) {
			int r = num % 10;
			num = num / 10;
			if (num == 0) {
				// check for the largest left most digit
				if (max < r) {
					max = r;
					ind = i;
				}
			}
		}
	}

	// print the largest number

	// print the rotation of array
	for (int i = ind; i < n; i++)
		cout << a[i];

	// print the rotation of array
	for (int i = 0; i < ind; i++)
		cout << a[i];
}

// Driver Code
int main()
{
	int a[] = { 54, 546, 548, 60, 1, 9999, 10000 };
	int n = sizeof(a) / sizeof(a[0]);
	printLargest(a, n);
	return 0;
}
