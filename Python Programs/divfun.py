class time:
    pass
def print_time(t):
    print("%d:%d:%d"%(t.hr,t.min,t.sec))

def time_to_int(t):
    min=t.hr*60+t.min   # 2 times call for start and delay
    print(min)
    sec=min*60+t.sec    # adding those value
    print(sec)
    return sec

def int_to_time(sec):
    t=time()
    print(sec)
    min,t.sec=divmod(sec,60)    #qtn and remainder 48330/60=805 &0.5  ...0.5*60=30
    print(min,t.sec)
    t.hr,t.min=divmod(min,60)   #805/60=13hr and 0.416*60=25
    print(t.hr, t.min)
    return t
    min=t.hr*60+t.min
    sec=min*60+t.sec
    return sec
def add_t(t1,t2):       #et is MOVIE END TIME OBJECT
    print(t1,t2)
    sec=time_to_int(t1)+time_to_int(t2)
    return int_to_time(sec)

start=time()
start.hr=9
start.min=50
start.sec=30
dur=time()
dur.hr=3
dur.min=35
dur.sec=00

done=add_t(start,dur)
print_time(done)
