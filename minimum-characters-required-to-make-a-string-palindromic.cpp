#include<bits/stdc++.h>
using namespace std;
int fmod(int a)
{
    if(a<0) a*=-1;
    return a;
}
int solve(string A) {
    vector<int> middleCharPos;
    cout<<middleCharPos.size();
    for(int i=1;i<A.size()-1;++i){
        if(A[i-1]==A[i+1])
            middleCharPos.push_back(i);
    }
    if(middleCharPos.size()==0)
        return A.size()-1;
    else
    {
        int centerMiddleCharPos=middleCharPos[0];
        for(int i=0;i<middleCharPos.size();++i)
        {
            if(fmod(middleCharPos[i]-A.size()/2)<fmod(centerMiddleCharPos-A.size()/2))
                centerMiddleCharPos=middleCharPos[i]-A.size()/2;
        }
        
        return centerMiddleCharPos;
    }
    
    
}
int main(){
    string A="ABC";
    cout<< solve(A);
}
