#주석
#세미콜론 x
# a=10
# print(a)
# a= ['g','a','g']
# type(a)

# money = int(input())
# if money >3000 :
#     print("택시 타고 가자")
# elif money == 3000 :
#     print("버스 타고 가자")
# else:
#      print("집가자")



# text = "내가 또 밤새면 개다"
# # if "밤새" in text:
# #     print("멍멍")
# message = "멍멍" if "밤새" in text else "사람"
# print(message)

# def love(which) :
#     print("i love "+who)

# till_i_die = True
# snack = input()
# while till_i_die :
#     love(snack)

# add = 0
# for i in range(1,11,1) :
#     add+= i
# print(add)

# test_list= ['one', 'two', 'three']

# for test in test_list:
#     print(test)


# for i,v in enumerate(test_list) :
#     print("index : {}, vlaue : {}".format(i,v))

  # a, b =b,a

# for i in range(len(test_list)) :
#       print(test_list[i])
#text = "점심뭐먹지"
# text="심점먹지뭐"

# arr=list(text)
# # arr[0] 심 [1] 점

# arr[0] ,arr[1] =arr[1], arr[0]
# arr.insert(2,arr[4])
# arr.pop()
# print(''.join(arr))

# #####################################################################
# arr1 = list("Hello World")
# #arr2 = arr1 #얕은복사
# arr2= [i for i in arr1]
# print(arr1)
# print(arr2)

# arr2[7]='a'

# print(arr1)
# print(arr2)


# print(id(arr1)) #주소값
# print(id(arr2))

# str1 = "Hello swing"
# str2 = "Hello swing2"
# str3 = """
# Hello
# Swing
# """

# str4='''
# Hello
# Again
# '''

# print("str1 : ")
# print(str1)

# print("str2 : ")
# print(str2)

# print("str3 : ")
# print(str3)

# print("str4 : ")
# print(str4)

# print("hi 김혜민 "*5)
# str1="ㄴㅇㄹㅇㄴㄹㄴㅇㄹㄴㅇㄹㄴ하ㅏㅣ ㅜㅇㄹ후일"
# print("len(str1): ")
# print(len(str1))

# str="천재인 신유림 바보인 김혜송"
# print(str[4:10])


# str1 ="swidbng"
# print(str1.find('b')) #없으면 -1


# str2="Hello world"

# print(str2[5:]) #인덱스 0에서 부터 인덱스5직전의 문자를 가져온다


str1="천재인 신유림 바보인 김혜송"

print(str1[:3]+str1[11:13]+str1[5:11]+str1[3:5]+str1[-2:])
#"천재인 김유림 바보인 신혜송"


str2="hello"
str3="안녕"
print(str2,end="")
print(str3)

