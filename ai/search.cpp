#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

int BinarySearch(vector<int>& v, int n)
{
    int left = 0;
    int right = v.size() - 1;
    if (n == v[0])
	    return 0;
    if (n == v[v.size() - 1]) 
	    return v.size() - 1;

    while (left <= right)
    {
	    int mid = (right + left) / 2;

	    if (v[mid] == n)
		    return mid;
	    if (v[mid] < n)
		    left = mid + 1;
	    else
		    right = mid - 1;
    }

    return -1;
}

int linearSearch(vector<int>& v, int n)
{
    for (int i = 0; i < v.size(); i++)
	    if (n == v[i])
		    return i;

    return -1;
}

int main()
{
    vector<int> arr;
    for (int i = 0; i < 10000; i++)
	    arr.push_back(i);

    int n = arr.size()-1;
    
    auto startBinary = high_resolution_clock::now();
    cout<<"binary search result "<<BinarySearch(arr, n)<<endl;
    auto endBinary = high_resolution_clock::now();
    
    auto startLinear = high_resolution_clock::now();
    cout<<"linear search result "<<linearSearch(arr, n)<<endl;
    auto endLinear = high_resolution_clock::now();

    cout << "Binary Search Time: " << duration_cast<microseconds>(endBinary - startBinary).count() << " microseconds" << endl;
    cout << "Linear Search Time: " << duration_cast<microseconds>(endLinear - startLinear).count() << " microseconds" << endl;

}