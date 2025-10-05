#include <iostream>
#include <unordered_map>
using namespace std;
int main()
{
    int n;
    cin >> n;
    unordered_map<string, int> user_names;
    for(int i=0;i<n;i++){
        string name;
        cin >> name;
        if (user_names.find(name) == user_names.end())
        {
            user_names[name] = 1;
            cout << "OK" << endl;
        }
        else
        {
            cout << name << user_names[name] << endl;
            user_names[name]++;
        }
    }
    return 0;
}