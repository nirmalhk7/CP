import time
def get_time(fnx):
    start=time.time()
    print(fnx())
    print("Time",time.time()-start)