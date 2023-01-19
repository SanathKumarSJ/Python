def checkin(num):
    for i in range(2,num):
        if(num%i==0):
            return 0
        else:
            return 1
num=int(input("Enter the number"))
isprime=checkin(num)
if(isprime==1):
    print(num," Is a prime number")
else:
    print(num," Is not a prime numeber")
