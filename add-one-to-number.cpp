#include<bits/stdc++.h>
using namespace std;
void plusOne(vector<int> &A)
{
    A[A.size()-1]+=1;
}
int main(){
    vector<int> r{1,0};
    plusOne(r);
    for(int i=0;i<r.size();++i)
    {
        cout<<r[i]<<" ";
    }
}