def stringPop(A,i):
    return A[:i]+A[(i+1):]
def convert(A,B):
    charFound=[False for i in range(len(A))]
    if(len(A)<=B or B==1):
        return A
    output=["" for i in range(B)]
    rCount=0
    goDown=True
    for i in range(len(A)):
        output[rCount]+=A[i]
        if(rCount==0):
          #  print("Tilt Down")
            goDown=True
        if(rCount==B-1):
         #   print("Tilt Up")
            goDown=False
        if(goDown):
        #    print("Going Down",output[rCount],rCount,A[i])
            rCount+=1
        else:
       #     print("Going Up",output[rCount],rCount,A[i])
            rCount-=1
    outputConc=""
    for i in range(len(output)):
        outputConc+=output[i]
    return outputConc
if __name__ == "__main__":
    print(convert("kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS",2))
    #print(stringPop("nirmal",5))