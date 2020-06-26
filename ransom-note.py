def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransomNoteD={}
    for r in ransomNote:
        try:
            ransomNoteD[r]+=1
        except:
            ransomNoteD[r]=1
    magazineD={}
    for m in magazine:
        try:
            magazineD[m]+=1
        except:
            magazineD[m]=1
    for key in ransomNoteD:
        print("Comparing for ",key)
        try:
            if(magazineD[key]!=ransomNoteD[key]):
                return False
        except:
            return False;
    return True
if __name__ == "__main__":
    print(canConstruct("aab","ab"))
    pass