#include<bits/stdc++.h>
using namespace std;

string multiply(string A, string B) {
    long long val1=0;
    long long val2=0;
    for(int i=0;i<A.size();++i)
    {
        int posval=(int)(A[i]-'0');
        if(!val1 && posval==0)
        {
            continue;
        }
        else{
            val1=val1*10+posval;
        }
    }
    for(int i=0;i<B.size();++i)
    {
        char val=B[i];
        int posval=(int)(B[i]-'0');
        if(val2==0 && posval==0)
        {
            continue;
        }
        else{
            val2=val2*10+posval;
        }
    }
    long long result=val1*val2;
    cout<<result;
}
int main(){
    multiply("10","10");
}