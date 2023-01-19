def a():
    a=int(input("Enter value of a= "))
    b=int(input("Enter value of b= "))
    res1=a+b
    res2=a-b
    res3=a*b
    return (res1,res2,res3)
s,m,g=a()
print("sum = ",s,"minus = ",m,"Multiply = ",g)