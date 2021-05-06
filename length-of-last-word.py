# 58
# Status: Completed

 sarray = s.split(" ")
  newarr = []
   for i in sarray:
        if(i != ""):
            newarr.append(i)

    # print(newarr,sarray)
    if(len(newarr) == 0):
        return 0
    return len(newarr[-1])
