void palindrome(char s[])
{
  int i,arr[26]={0};
  
  for(i=0;i<strlen(s);i++)
  {  
  
    s[i]=tolower(s[i]);
  	arr[int(s[i])%int('a')]++; 
  
  }
 

void main(){
    palindrome("yalmalaam") // malayalam
    palindrome("iiktte")  //ietnitk
}