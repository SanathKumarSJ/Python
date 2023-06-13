
class time:
    pass
def add_t(t1,t2):       #et is MOVIE END TIME OBJECT
    et=time()
    et.hr=t1.hr+t2.hr
    et.min=t1.min+t2.min
    et.sec=t1.sec+t2.sec
    return et
def print_time(t):
    print("%d:%d:%d"%(t.hr,t.min,t.sec))
start=time()
start.hr=9
start.min=30
start.sec=60
if(start.min>=60):
    start.min=start.min-60
    start.hr+=1
if(start.sec>=60):
    start.sec=start.sec-60
    start.min+=1
dur=time()
dur.hr=3
dur.min=70
dur.sec=00
if(dur.min>=60):
    dur.min=dur.min-60
    dur.hr+=1
if(dur.sec>=60):
    dur.sec=dur.sec-60
    dur.min+=1
done=add_t(start,dur)
print_time(done)