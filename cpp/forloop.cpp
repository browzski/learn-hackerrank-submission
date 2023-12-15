#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    const char *c[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    for (int i = a; i <= b; i++)
    {
        if (i > 9)
        {
            if (i % 2 == 0)
            {
                cout << "even";
            }
            else
            {
                cout << "odd";
            }
            cout << endl;
            continue;
        }
        cout << c[i];
        cout << endl;
    }
    return 0;
}