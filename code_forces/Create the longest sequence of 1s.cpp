#include <iostream>
using namespace std;
int main()
{
    string bits;
    cin >> bits;
    short i = 0, ii, count = 0, total = 0, max = 0;

    for (i = 0; i < bits.length(); i++)
    {
        if (bits[i] == '1')
        {
            total++;
            max = (total > max) ? total : max;
        }
        else if (count == 0)
        {
            count++;
            ii = i;
            total++;
        }
        else
        {

            count = 0;
            max = (total > max) ? total : max;
            i = ii;
            total = 0;
        }
    }

    cout << max << endl;
}