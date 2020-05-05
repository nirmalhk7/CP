#include<bits/stdc++.h>
using namespace std;

int isNumber(const string A) {
    bool expomode=false;
    int IntEncountered=0;
    for(int i=0;i<A.size();++i)
    {
        //Negative Number
        if(A[i]=='-' || A[i]=='+')
        {
            // - at end is error.
            if(i==A.size()-1)
                return 0;
            else
            {
                //Number after - must be digit.
                if(!isdigit(A[i+1]))
                    return 0;
            }
        }
        //Exponential and Decimal
        else if(A[i]=='e' || A[i]=='E' || A[i]=='.')
        {
            //TODO Work for 0.4e-3 (true) and 0.4e3.3 (false)
            //Check leftmost and rightmose
            if(( i==0 || i==A.size()-1 ) && A[i]!='.') return 0;
            else if(i==A.size()-1 && A[i]=='.') return 0;
            else if(expomode) return 0;
            else if(i!=0){
                if(!isdigit(A[i-1])) return 0;
                // + or - at A[i+1] is okay.
                else if(A[i+1]!='-' && A[i+1]!='+' && !isdigit(A[i+1])) return 0;
            }
            if(A[i]=='e'|| A[i]=='E')   expomode=true;
        }
        else if(A[i]==' ')  continue;
        else if(!isdigit(A[i]))  return 0;
        else if(isdigit(A[i]))  IntEncountered=1;
    }

    return IntEncountered;
}
int main(){
    // cout<<isNumber("4e324")<<endl;
    cout<<isNumber(".2")<<endl;
    cout<<isNumber("3e42")<<endl;
    cout<<isNumber("+ 3")<<endl;
    cout<<isNumber("+43w")<<endl;
    cout<<isNumber("2e10")<<endl;
    cout<<isNumber("0.4e-3")<<endl;
    cout<<isNumber("0.4e3.3")<<endl;
    cout<<isNumber("4e3e4")<<endl;
    cout<<isNumber("-45")<<endl;
}