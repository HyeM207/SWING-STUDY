import os
# print(os.getcwd())
# a=os.listdir("c:\\Users\\김혜민\\Desktop\\200327")

# for text in a:
#     print(os.access())
#     print(text)

for (path,dir,files) in os.walk("c:\\"):
    for filename in files:
        ext=os.path.splitext(filename)[-1]
        if ext =='py':
            print("%s%s" % (path,filename))