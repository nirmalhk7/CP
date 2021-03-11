# 152
# Medium Difficulty
# Incompleted Status.


def soln(arr):
    def gpx(l):
        return l[0]+','+str(l[1])+','+str(l[2])+','+l[3]
    suspected = {}
    name_hsx = {}
    sorted_time = []
    sorted_arr = []
    for i, t in enumerate(arr):
        name, time, amount, city = t.split(',')
        sorted_arr.append([name, int(time), int(amount), city])
    sorted_arr= sorted(sorted_arr,key=lambda x:x[1])
    lasttrans_arr = {}
    for i in range(len(sorted_arr)):
        if(sorted_arr[i][2] > 1000):
            suspected[gpx(sorted_arr[i])] = True
        try:
            last_name, last_time, last_amount, last_city = lasttrans_arr[sorted_arr[i][0]]
            print("Comparing",sorted_arr[i],lasttrans_arr[sorted_arr[i][0]])
            if(sorted_arr[i][1]-last_time<=60  and last_city != sorted_arr[i][3]):
                suspected[gpx(sorted_arr[i])] = True
                suspected[gpx(lasttrans_arr[sorted_arr[i][0]])] = True
            lasttrans_arr[sorted_arr[i][0]] = sorted_arr[i]
        except:
            lasttrans_arr[sorted_arr[i][0]] = sorted_arr[i]
    return list(suspected.keys())


# print(soln(["alice,50,100,beijing", "alice,20,800,mtv"]))
# print(soln(["alice,20,800,mtv", "alice,50,1200,mtv"]))
# print(soln(["alice,20,800,mtv", "bob,50,1200,mtv"]))
# print(soln(["alex,676,260,bangkok", "bob,656,1366,bangkok",
#             "alex,393,616,bangkok", "bob,820,990,amsterdam", "alex,596,1390,amsterdam"]))
print(soln(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))
