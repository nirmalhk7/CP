#include<bits/stdc++.h>
using namespace std;

int maximumGap(const vector<int> &A) {
    vector<int> maxd;
    bool foundMaxD=false;
    for(int i=0;i<A.size();++i)
    {
        foundMaxD=false;
        for(int j=A.size()-1;j>=i;--j)
        {
            if(A[i]<=A[j])
            {
                maxd.push_back(j-i);
                foundMaxD=true;
            }

        }
        if(foundMaxD==false)
        {
            maxd.push_back(-1);
        }
    }
    int max=maxd[0];
    for(int z=0;z<maxd.size();++z)
    {
        if(max<maxd[z])
            max=maxd[z];
    }
    return max;
}

int main(){
    vector<int> a={1};
    string x="HELLPD";
    cout<<"\n"<<x[2];
    cout<<maximumGap(a);
}
