#include<bits/stdc++.h>
using namespace std;

int numSetBits(unsigned int a) {
    int oneCount = 0;
    while (a != 0){
        if(a%2!=0){
            oneCount+=1;
        }
        a/=2;
    }
    return oneCount;
}
int main(){
    cout<<numSetBits(4294967295);
}