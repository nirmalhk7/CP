#include<bits/stdc++.h>
using namespace std;

void sortColors(vector<int> &A){
    int whitecount=0,redcount=0,bluecount=0;
    for(int i=0;i<A.size();++i)
    {
        if(A[i]==0) redcount++;
        else if(A[i]==1) whitecount++;
        else if(A[i]==2) bluecount++;
    }
    A.clear();
    for(int i=0;i<redcount;++i)
        A.push_back(0);
    for(int i=0;i<whitecount;++i)
        A.push_back(1);
    for(int i=0;i<bluecount;++i)
        A.push_back(2);
}
int main(){
    //vector<int> inp{0,1,2,0,1,2};
    vector<int> inp{2,1,0,0,1,2,1};
    sortColors(inp);
    for(int i=0;i<inp.size();++i)
    {
        cout<<inp[i]<<" ";
    }
}