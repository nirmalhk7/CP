#include<bits/stdc++.h>
using namespace std;

void subArrayPos(vector<int> &A,int l,int h){
    if(l==h)
        return arr[l];
    int m=(l+h)/2;
    return max(subArrayPos(A,l,m),subArrayPos(A,m+1,h))
}
void maxSubArray(vector<int> &A){
    subArrayPos(A,0,A.size()-1)
}
int main(){
    vector<int> r{-2, 1, -3, 4, -1, 2, 1, -5, 4};
    maxSubArray(r);
    for(int i=0;i<r.size();++i)
    {
        cout<<r[i]<<" ";
    }
}