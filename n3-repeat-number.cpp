#include<bits/stdc++.h>
using namespace std;

int repeatedNumber(vector<int> A){
    int flag=INT_MIN;
    int elcount=0;
    for(int i=0;i<12;++i)
    {
        int rint=A[rand()%A.size()];
        elcount=0;
        for(int i=0;i<A.size();++i)
        {
            if(rint==A[i])
            {
                flag=A[i];
                elcount++;
            }
        }
  //      cout<<"Element  "<<flag<<" found "<<elcount<<" times"<<endl;
        if(elcount>=A.size()/3)
            return flag;
    }
    return -1;
}
int main(){
    vector<int> inp{11,12,13,1,2,3,4,1,5,1,7,1,8,9,1};
    cout<<repeatedNumber(inp);
}