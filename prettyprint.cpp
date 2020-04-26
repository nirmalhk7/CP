#include<bits/stdc++.h>
using namespace std;
vector<vector<int> > prettyPrint(int A) {
    vector<int> colVector;
    vector<vector<int>> ans;
    int rcCount=2*A-1;
    for(int i=0;i<rcCount;++i)
    {
        colVector.push_back(i);
    }
    for(int i=0;i<rcCount;++i)
    {
        ans.push_back(colVector);
    }
    for(int i=0;)

}
int main(){
    vector<vector<int>> a=prettyPrint(3);
    for(int i=0;i<a.size();++i)
    {
        for(int j=0;j<a[i].size();++j)
        {
            cout<<a[i][j]<<" ";
        }
        cout<<"\n";
    }
}
