#include<bits/stdc++.h>
using namespace std;

string getnext(string P)
{
    string res;
    int i=1, count = 1;
    for(; i<P.size(); i++)
    {
        if(P[i-1] != P[i])
        {
            res = (res + to_string(count)) + P[i-1];
            count = 1;
        }
        else
            count++;
    }
    return ((res + to_string(count)) + P[i-1]);
}

string countAndSay(int A) {

}

int main(){
    cout<<getnext("3");
}