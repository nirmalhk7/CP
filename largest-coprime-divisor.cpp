#include<bits/stdc++.h>
using namespace std;
int cpFact(int A, int B) {
    if(__gcd(A,B)!=1)
    {
        if(A<B){
            int temp=A;
            A=B;
            B=temp;
        }
        vector<int> divisible;
      //  cout<<"\n"<<A<<B;
        for(int i=2;i<=B;++i)
        {
            divisible.push_back(i);
        }
        int x=0;
        while(__gcd(A,B)!=1)
        {
            if(A%divisible.at(x)==0 && B%divisible.at(x)==0 )
            {
                A/=divisible.at(x);
            }
            if(x==6 && __gcd(A,B)!=1)
            {
                x=0;
            }
            else{
                ++x;
            }
        }
    }
    return A;
}

int main(){
    cout<<cpFact(6,96);
}