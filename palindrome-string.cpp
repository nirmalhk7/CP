#include<bits/stdc++.h>
using namespace std;

int stringPali(string inp)
{
    string s;
    for(int i=0;i<inp.size();++i)
    {
        if(isalnum(inp[i]))
        {
            s.push_back(tolower(inp[i]));
        }
    }
    //cout<<s;
    for(int i=0;i<s.size()/2;++i)
    {
        if(s[i]!=s[s.size()-1-i])
        {
            return 0;
        }
    }
    return 1;
}
int main(){
    string s="race a car";
    cout<<stringPali(s);
}