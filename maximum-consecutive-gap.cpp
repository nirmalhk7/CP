#include<bits/stdc++.h>
using namespace std;

int mathmod(int A)
{
    if(A<0) A*=-1;
    return A;
}
int maximumGap(const vector<int> &r) {
    vector<int> A=r;
    sort(A.begin(),A.end());
    if(A.size()<2) return 0;
    int maxdiff=(A[1]-A[0]);
    if(A.size()>2)
    {

        for(int i=1;i<A.size();++i)
        {
            if(i!=(A.size()-1))
            {
                if(maxdiff<(A[i+1]-A[i]))
                {
                    maxdiff=(A[i+1]-A[i]);
                }
            }
        }
    }
    return maxdiff;
}
int main(){
    vector<int> A={1,10};
    cout<<maximumGap(A);
}