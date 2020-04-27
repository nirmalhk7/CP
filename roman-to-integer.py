# Siccess
def getNumVal(x):
    if(x=="I"): return 1
    elif(x=="V"): return 5
    elif(x=="X"): return 10
    elif(x=="L"): return 50
    elif(x=="C"): return 100
    elif(x=="D"): return 500
    elif(x=="M"): return 1000

def romanToNum(A):
    ans=0;
    prevVal=0
    for i in range(len(A)):
        numVal=getNumVal(A[i]);
        if(prevVal>=numVal):
            ans+=numVal
        else:
            ans+=numVal-2*prevVal
        prevVal=numVal
    return ans;

if __name__ == "__main__":
    print(romanToNum("MDCCCLIX"))