#include<bits/stdc++.h>
using namespace std;
int coverPoints(vector<int> &A, vector<int> &B);
int main(){
    vector<int> x{0,1,2};
    vector<int> y{0,1,2};
    coverPoints(x,y);
}
int fmod(int a)
{
    if(a<0)
        a*=-1;
    return a;
}
int coverPoints(vector<int> &A, vector<int> &B) {
    int sX=A[0],sY=B[0];
    int cX=sX,cY=sY;
    int eX=A[A.size()-1],eY=A[A.size()-1];
    int itr=0;
    int countmove=0;
    while(cX!=eX && cY!=eY){
        int distX=fmod(cX-A[itr]),distY=fmod(cY-B[itr]);
        cout<<"\nCX "<<cX<<" CY "<<cY<<" EX "<<eX<<" EY "<<eY;
        while(distX!=0 && distY!=0)
        {
            distX--; distY--; 
            countmove++;
            cout<<"\nCOUNTa "<<countmove<<" dX"<<distX<<" dY"<<distY;
        }
        if((distX==0 || distY==0) && !(distX ==0 && distY==0))
        {
            countmove+=distX+distY;
            cout<<"\nCOUNTb "<<countmove<<" dX"<<distX<<" dY"<<distY;
        }
        cX=A[itr+1];
        cY=B[itr+1];
        
    }   
    return 0;
}
