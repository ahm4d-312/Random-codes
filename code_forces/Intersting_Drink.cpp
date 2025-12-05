#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
using namespace std;

int binary_search(vector<int>& prices,int target)
{
    int low =0 ,top=prices.size()-1,mid;
    while(low<=top)
    {
        mid=(low+top)/2;
        if(prices[mid]==target)
            return mid +1;
        else if (prices[mid]>target)
            top=mid-1;
        else
            low=mid+1;
    }
    return -1;
}

int main()
{
    int n; 
    cin >>n;
    vector<int> prices(n);
    for(int i =0;i<n;i++)
        cin >> prices[i];
    sort(prices.begin(),prices.end());
    int days;
    cin >> days;
    int budget;
    for(int i=0;i<days;i++){
        cin>>budget;
        cout<<binary_search(prices,budget)<<endl;
    }

}