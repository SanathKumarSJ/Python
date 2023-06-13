
class time:
    pass
def add_t(time,sec,min):       #et is MOVIE END TIME OBJECT
    time.sec=time.sec + sec
    time.min= time.min+min
    while time.sec>=60:
        time.sec-=60
        time.min=time.min+1
    while time.min>=60:
        time.min-=60
        time.hr=time.hr+1
def print_time(t):
    print("%d:%d:%d"%(t.hr,t.min,t.sec))
start=time()
start.hr=9
start.min=14
start.sec=30
print("BEFORE STANDARD FORMAT")
print_time(start)
add_t(start,5,6)
print_time(start)