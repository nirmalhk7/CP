import math
def romanDictionary(num):
    switcher = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    return switcher.get(num,"")

def fmod(x):
    if(x<0): x*=-1
    return x

def getBestRoman(num):
    index=[1,5,10,50,100,500,1000]
    numRoman=None
    if(num>index[-1]):
        numRoman=romanDictionary(index[-1])*(num//index[-1])
    min_diff=9999999999999999999999999999
    bestFit=""
    min_fit_index=-999
    for i in range(len(index)-1):
        if(min_diff>fmod(index[i]-num)):
            min_diff=fmod(index[i]-num)
            min_fit_index=index[i]
            min_fit_index_index=i
    print("DiffCalced",num,min_diff,min_fit_index)

    if(num<index[i]):
        if(min_diff<3):
            bestFit="I"*min_diff+romanDictionary(min_fit_index)
        else:
            bestFit=romanDictionary(fmod(num-min_fit_index))+romanDictionary(min_fit_index)
        print(fmod(num-min_fit_index),min_fit_index)
    else:
        x=fmod(num-min_fit_index) # 200
        xgcd=math.gcd(num,min_fit_index) # 100
        bestFit=romanDictionary(min_fit_index)+romanDictionary(xgcd)*int(x/xgcd)
    numRoman=bestFit
    print("Number ",bestFit)
    return numRoman

def ans(A):
    numarr=[]
    tenCount=0
    while A!=0:
        numarr.append(int((A%10)*10**tenCount))
        A=A-A%10
        tenCount+=1
        A/=10
    numarr.reverse()
    stropx=""
    for i in range(len(numarr)):
        stropx+=getBestRoman(numarr[i])
    return stropx

if __name__ == "__main__":
    print(ans(8))
    print(ans(464))
    print(ans(323))
    print(ans(4))
