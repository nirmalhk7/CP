def soln(S,L):
    hx={}
    tempS= S
    removedNos=0
    for i in L:
        
        while tempS.find(i)!=-1:
            # print("Finding",i)
            posn= tempS.find(i)
            if(i in hx):
                hx[i].append(posn+removedNos)
                print("Appending posn",hx[i],i)
            else:
                hx[i]=[posn+removedNos]
                print("Appeding posn",hx[i],i)
            tempS= tempS[:posn]+tempS[posn+3:]
            removedNos+= 3
            print(tempS)
            # input()
    return hx

def soln2(S,L):
    def generateSubstring(strx,sx):
        ans=[]
        for i in range(0,len(strx)-sx):
            ans.append(strx[i:i+sx])
        return ans
    res= []
    if len(L[0])*len(L)>len(S):
        return res
    hsx= {}
    # substr= generateSubstring(S,6)
    for i in range(len(L)):
        if L[i] in hsx:
            hsx[L[i]]+= 1
        else:
            hsx[L[i]]= 1
    # for i in range(substr):
    #     temp_hsx=hsx.copy()
    #     if(i in temp_hsx):
    #         temp_hsx[i]-=1
    #     else:
    #         break
    for i in range(0,len(S)-3+1):
        temp_hsx= hsx.copy()
        j=i
        count= len(L)
        while j<i+len(L[0])*len(L):
            word=S[j:j+3]
            
            if(word not in hsx or temp_hsx[word]==0): break
            else:
                # print("Found")
                temp_hsx[word]-= 1
                count-= 1
            j+=len(L[0])
            # print("Word",word,"HSX",hsx,"THSX",temp_hsx,"Count",count)
        if count==0:
            res.append(i)
    return res
import time
def soln3(A,B):
    if len(A) < (len(B) * len(B[0])):
        return []

    #get all permutations of concatenation of words in B as strings
    from itertools import permutations
    perm=["".join(i) for i in permutations(B)]
    len_word=len(perm[0])
    output=[]
    for i in range(len(A)-len_word+1):
        substr=A[i:i+len_word]
        if substr in perm:
            output.append(i)
    return output
if __name__ == "__main__":
    stx=time.time()
    print(soln3("barfoothefoobarman",["foo", "bar"]))
    print(time.time()-stx)
  #  print("----")
   # print(soln("khedkarbarnirmalfoobarnirmalfookhedkar",["bar","foo","nirmal"]))
    # Soln: 7, 19