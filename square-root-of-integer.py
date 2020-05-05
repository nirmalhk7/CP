def sqrt(A):
    LOW=0
    HIGH=A+1
    ans=0
    counter=0
    prevVal=[0,0,0]
    while LOW<=HIGH:
   #     print("LOW ",LOW," HIGH ",HIGH)
        MED=(LOW+HIGH)//2
        ans=MED**2
        prevVal[counter]=MED
        counter+=1
        if counter>2:
            counter=0
  #      print(MED,ans)
        if(ans==A or prevVal==[MED,MED,MED]):
            return MED
        elif(ans<A):
            LOW=MED
        elif(ans>A):
            HIGH=MED

if __name__ == "__main__":
    print(sqrt(40))