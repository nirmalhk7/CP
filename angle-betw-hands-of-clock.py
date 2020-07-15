def soln(hour,minutes):
    def processHrs(hrs,mins):
        if(hrs==12): hrs=0
        return 
    hourAnglewrt12= minutes*0.5
    print(hourAnglewrt12)
    minuteAnglewrt12= abs(minuteAnglewrt12)

def soln2(hour,minutes):
    if(hour==12): hour=0
    hourAngle= hour*30+minutes*0.5
    minuteAngle= minutes*6
    print(hourAngle,minuteAngle)

    answer1= abs(minuteAngle-hourAngle)
    answer2= abs(360-minuteAngle+hourAngle)
    answer3= abs(360-hourAngle+minuteAngle)
    answer = min(answer1,answer2,answer3)
    print("ANS",answer1,answer2,answer3)
    if(answer%1==0): return int(answer)
    else: return answer
if __name__ == "__main__":
    # print(soln2(12,30))
    # print(soln2(3,30))
    # print(soln2(3,15))
    print(soln2(11,50))
    print(soln2(1,57))
    print(soln2(11,20))