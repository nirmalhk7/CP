def numJewelsInStones(J: str, S: str) -> int:
    stoneDictionary={}
    for i in S:
        try:
            stoneDictionary[i]+=1
        except:
            stoneDictionary[i]=1
    ans=0
    for j in J:
        try:
            ans+=stoneDictionary[j]
        except:
            continue
    return ans
if __name__ == "__main__":
    J="aA"
    S="aAAbbbb"
    print(numJewelsInStones(J,S))