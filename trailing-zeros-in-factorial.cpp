#include<bits/stdc++.h>
using namespace std;
int factorial(int x){
    int ans=1;
    for(int i=x;i>=1;--i)
    {
        ans*=i;
    }
    return ans;
}
int trailingZeroes(int A) {
    int ans=0;
    A=factorial(A);
    while(A%10==0){
        ans++;
        A/=10;
    }
    return ans;
}
int ans=0;
int get0Count(int A){
    while(A%10==0){
        ans++;
        A/=10;
    }
    return A;
}
int fn(int A){
    int i;
    int mult=1;
    int zcount=0;
    for(i=A;i>1;--i)
    {
        mult*=i;
        if(mult%10==0){
            zcount++;
            mult/=10;
        }
    }
    return zcount;
}
int zn(int A){
    
    for(int i=5;i>1;++i)
    {

    }
}
int main(){
    int ans=fn(10);
    cout<<"\n"<<ans;
}