names=[]
record=[]
f=open("C:/Users/김혜민/Desktop/python 코드/python스터디/swing.txt",'r')
lines=f.readlines()
i=0
for line in lines:
    # print(line[:line.index(":")])
    # print(line[line.index(":")+1:])
    names.append(line[:line.index(":")])
    record.append(line[line.index(":")+1:])
    i+=1
f.close()

print(names)
print(record)

name.append("helloworld\n")

f=open("C:/Users/김혜민/Desktop/python 코드/python스터디/swing.txt",'a')
for 




