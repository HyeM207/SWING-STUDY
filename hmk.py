# first=int(input("Input first number >> "))
# second=int(input("Input second number >> "))

# print("%d + %d = %d" %(first,second,first+second))
# print("%d - %d = %d" %(first,second,first-second))
# print("%d * %d = %d" %(first,second,first*second))
# print("%d / %d = %.2f" %(first,second,first/second))
for i in range(1, 10):
    for j in range(2, 10):
        print("%d x %d = %2d" %(j,i,i*j),end="\t")
    print()
