#include<bits/stdc++.h>
using namespace std;
int soln(int A){
    vector<int>a(50,1);
    int i=2;
    while(a[i-1]<A){
        a[i]=a[i-1]+a[i-2];
        i++;
    }
    queue<pair<int,int>> q;
    q.push(make_pair(A,0));
    while(!q.empty()){
        pair<int,int> p= q.front();
        int x=p.first, level= p.second;
        if(x==0) return level;
        q.pop();
        for(int k=i-1;k>=1;k--){
            if(x-a[k]>=0){
                q.push(make_pair(x-a[k],level+1));
                break;
            }
        }
    }
    return -1;
}
int main(int argc, char const *argv[])
{
    cout<< soln(4);
    return 0;
}
