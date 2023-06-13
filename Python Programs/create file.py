'''k=open("temp.doc","w")   #create file with respected extension
print("file created succesfully...") #command after creation
def fact(num):						#function of factorial
	fact=1
	for i in range(1,num+1):
		fact=fact*i
	return fact
num=int(input("Enter the number"))	#Input
k.write(str(num))
k=open("temp.doc","r")
print("read the entire file")
print(k.read())						#reading the output
k.close'''
from PIL import Image
myImage = Image.open("C:\Users\fain\Pictures\photo.jpg");
k=open("temp.doc","w")   #create file with respected extension
print("file created succesfully...") #command after creation
k.write(str(myImage))
k=open("temp.doc","r")
print("read the entire file")
print(k.read())
