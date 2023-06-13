'''filename='sample.txt'
fh=open(filename)
for line in fh:
    print(line)'''
i=input('Enter the word: ')
dic={}
for letter in i:
    if letter in dic:
        dic[letter]+=1
    else:
        dic[letter] =1
print(dic)
for key,value in dic.items():
    print("the letter {} appered {} times".format(key,value))
