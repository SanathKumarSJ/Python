'''print("the try catch block will generate an exception x not defined")
print("-------------")
try:
    print(x)
except:
    print("An ecception occured")
print("--------------")
print("Name error")
print("The try catch block will generate an exeption x not defined")
print("-------------")
try:
    print(x)
except NameError:                       #name error used to check the variable presence
    print("Variable x is not defined ")
except:
    print("Something went wrong ")
print("-------------")
print("Name error")'''
print("Name error")
print("The try catch block will generate an exeption x not defined")
print("-------------")
try:
    a= 20
    b=5
    print(a/b)
except NameError:
    print("Variable x is not defined ")
except:
    print("Something went wrong ")
finally:
    print("The try exept is completed")
print("---------")