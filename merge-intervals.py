class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insert(self, intervals, new_interval):
    if (len(intervals)==0):
        return [new_interval]

    elif(new_interval.end<intervals[0].start):
        return intervals.insert(0,new_interval)
    elif(new_interval.end==intervals[0].start):
        intervals[0].start=new_interval.start;
        return intervals;

    elif(intervals[-1].end<new_interval.start):
        return intervals.append(new_interval)
    elif(intervals[-1].end==new_interval.start):
        intervals[-1].end=new_interval.end;
        return intervals;

    elif(new_interval.start<=intervals[0].start and intervals[-1].end<=new_interval.end):
        return [new_interval]

    for i in range(len(intervals)):
        if(intervals[i].start==new_interval.end and ):
            intervals[i].start=new_interval.start;
            new_interval.end=intervals[i].end;
        if(intervals[i].end=new_interval.start):
            intervals[i].end=


if __name__ == "__main__":
    i=[Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
    i=insert(i,Interval([4,9]))
    for x in range(i):
        print(x.start,x.end)