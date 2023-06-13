filename='sample.txt'
arr=[]
fh=open(filename)
for line in fh:
    print(line)
    words=line.split()
    print(words)
    for rp in words: 
        if rp not in arr:
            arr.append(rp)
print(arr)
for rp in arr:
    print(rp)