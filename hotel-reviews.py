
def solve(A,B):
    A=A.split('_')
    goodDictionary= {}
    for goodword in A:
        goodDictionary[goodword]=1
    newDictionary={}
    for i in range(len(B)):

        reviewWords=B[i].split("_")
        for word in reviewWords:
            newDictionary[B[i]]+=goodDictionary.get(word,0)
    sortedWords=[]
    print(A,B,goodDictionary,newDictionary)

    return sortedWords;
if __name__ == "__main__":
    print(solve("cool_ice_wifi",["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]))