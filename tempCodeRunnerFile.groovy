#include <iostream>
using namespace std;
int main()
{
    int i = 1,s=0; 
    for (i; i <= 7; i++) 
    {
        if(i%2==0) s = s + i; 
    }
    cout <<"1到7偶数之和:"<< s<<endl;
}
