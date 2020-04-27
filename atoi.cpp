#include<bits/stdc++.h>
using namespace std;

int atoi(string A)
{
    long long result=0;
    bool isPositive=true;
    string tempString="";
    for(int i=0;i<A.size();++i)
    {
        if(i==0 && (A[i]=='+'|| A[i]=='-'))
        {
            if(A[i]=='+')
                isPositive=true;
            else if(A[i]=='-')
                isPositive=false;
        }
        else if(isdigit(A[i]))
        {
            tempString+=A[i];
            cout<<tempString<<endl;
        }
        else
        {
            break;
        }
    }
    cout<<"TEMP"<<tempString;
    for(int i=0;i<tempString.size();++i)
    {
        result=result*10+(int)(tempString[i]-'0');
        if(result>=INT_MAX && isPositive)
            return INT_MAX;
        else if(result>=INT_MAX && !isPositive)
            return INT_MIN;
    }
    return 0;
}
int main(){
    atoi("7 U 0 T7165 0128862 089 39 5");
}