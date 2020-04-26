#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cout<<"\n"<<INT_MAX<<"\n"<<INT_MIN;
    vector<int> ans;
    cin>>N;
    vector<bool> isPrime(N+1,true);
    isPrime[0]=false;
    isPrime[1]=false;

    for(int i=2;i<=N;i++)
    {
        if(!isPrime[i]) continue;
        if(i>N/i) break;
        for (int j=i*i;j<=N;j+=i)
        {
            isPrime[j]=false;
        }
    }
    for(int i=2;i<=N;++i)
    {
        if(isPrime[i]&& isPrime[N-i])
        {
           
            ans.push_back(i);
            ans.push_back(N-i);
        }
    }
    for(int i=0;i<ans.size();++i)
    {
        cout<<"\t"<<ans[i];
    }
}