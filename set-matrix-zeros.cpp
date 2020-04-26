#include<bits/stdc++.h>
using namespace std;

void setZeroes(vector<vector<int> > &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    vector<tuple<int,int>> zeroCoordinates;
    for(int i=0;i<A.size();++i)
    {
        for(int j=0;j<A[i].size();++j)
        {
            if(A[i][j]==0)
            {
                // cout<<"\nA["<<i<<"]["<<j<<"]="<<A[i][j];
                zeroCoordinates.push_back(make_tuple(i,j));
            }
        }
    }
    // for(int i=0;i<zeroCoordinates.size();++i)
    // {
    //     cout<<"\n"<<get<0>(zeroCoordinates[i])<<" "<<get<1>(zeroCoordinates[i]);
    // }
    while(zeroCoordinates.size())
    {
        tuple<int,int> coor=zeroCoordinates.back();
        for(int i=0;i<A.size();++i)
        {   
            cout<<"\n";
            for(int j=0;j<A[i].size();++j)
            {
                if(i==get<0>(coor) || j==get<1>(coor))
                {
                    A[i][j]=0;
                }
                cout<<A[i][j]<<"\t";
            }
        }
        zeroCoordinates.pop_back();
    }


}
int zxo(vector<vector<int>> A){
    vector<int> colId;
    bool foundZero;
    for(int i=0;i<A.size();++i)
    {
        foundZero=false;
        for(int j=0;j<A[i].size();++j)
        {
            if(A[i][j]==0 && foundZero=true)
            {
                foundZero=true;
                for(int k=0;k<A[i].size();++k)
                {
                    A[i][k]=0;
                    //Row elements zero;
                }
            }
        }
    }
}
int main(){
    vector<vector<int> > vect{ { 1, 1, 1 }, 
                               { 1, 0, 1 }, 
                               { 1, 1, 1 } }; 
    setZeroes(vect);
}