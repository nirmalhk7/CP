#include <bits/stdc++.h>
using namespace std;

vector<int> wave(vector<int> &A);

void printall(vector<int> A){
    cout<<endl;
    for (int i=0;i<A.size();i++)
    {
        cout<<A[i]<<" ";
    }
    cout<<endl;
}
int main(){
    vector<int> w{1,10,7,9,12,17,15};
    w=wave(w);
    cout<<endl;
    printall(w);
}
vector<int> wavex(vector<int> &A){
    sort(A.begin(),A.end());
    for(int i=0;i<A.size();i+=2)
    {   
        if(i+1==A.size())
        {
            continue;
        }
        swap(A[i],A[i+1]);
    }
}
vector<int> wave(vector<int> &A) {
    sort(A.begin(),A.end());
    int x;
    for(int i=0;i<A.size();i+=2)
    {   
        if(i+1==A.size())
        {
            continue;
        }
        swap(A[i],A[i+1]);
    }
    return A;
}
