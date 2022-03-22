import random  #랜덤으로 수를 만들기 위해 random 라이브러리 추가

'''
    피드백 1 : 범위가 아닌 수가 입력되었을 때, 맞춘 횟수 증가 no
    피드백 2 : 최고기록만 점수판에 넣기
'''


# # 함수 정의1 (처음 프로그램 동작시 기록 불러오는 함수)
    # 1. open으로 파일을 열어, 파일 전체 내용을 lines에 리스트로 저장한다.
    # 2. :를 기준으로 이름은 names리스트의 0인덱스에, 숫자(랭킹)은 ranking배열의 0인덱스에 int형으로 저장한다.
def loading():
    f=open("C:/Users/xxx/swing.txt",'r')
    lines=f.readlines() #파일 전체 내용 lines에 저장
    for line in lines:
        names.append(line[:line.index(":")])    #이름은 ranking의 0인덱스에
        ranking.append(int(line[line.index(":")+1:-1])) # 랭킹은 int형으로 ranking 0인덱스에 삽입 ( -1인 한 이유는 \n 제거 위함 )
    f.close()


# # 함수 정의2 (프로그램 종료 전, 기록 저장하는 함수)
    # 1. 파일을 열고, names와 ranking리스트에 저장된 각 요소들을 한줄로 만들어 파일에 저장한다.
def close():
    f=open("C:/Users/xxx/swing.txt",'w')
    for name,rank in zip(names,ranking): #names와 ranking리스트에서 각 요소를 
         w=name+":"+str(rank)+"\n" # :와 \n로 합쳐 한줄로 만든다.
         f.write(w)     #파일에 한줄씩 기록
    f.close()




num=0  #시작화면 입력받는 변수로  while문에 쓰이는데, while문 돌기 위해 미리 초기화 
ranking = []  #게임 기록 저장할 빈 리스트
names=[]    # 닉네임 저장할 빈 리스트
loading() # 파일기록 불러오는 함수
while num!=3:   # 숫자 3(게임종료)
    guess=0  #사용자 입력받는 변수
    answer=random.randrange(1,101)  # 정답은 random의 randrange함수를 이용해, 1~100까지의 난수를 while돌때 마다 갱신한다.
    max=100 #게임할 때,입력할 최대값을 알려주는 변수
    min=1   #게임할 때,입력할 최소값을 알려주는 변수
    print("\nanswer : "+str(answer))  
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    num=int(input(">> "))   #무엇을 할지 입력받는다.
    if num==1:    #게임시작
        tryCount=1
        while True :
            guess=int(input(str(tryCount)+ "번째 숫자입력(" +str(min)+ "~" +str(max) + ") : ")) #guess변수에 추측한 값이 들어간다.
            if guess>max or guess<min :  #만약, 범위에서 벗어난 값 입력시, 메시지 출력
                print("범위에 벗어난 값을 입력하였습니다. 범위에 맞게 입력해주세요.")       #<==================피드백1
                tryCount=tryCount-1         
            elif guess==answer :    #만약 정답이라면,
                print("정답입니다!!\n"+str(tryCount)+"번만에 맞추셨습니다") # 정답이라 알려주기.
                if len(ranking)==0 or ranking[0] > tryCount:   #만약, 기록 최대값이 들어간 0번째 값보다 기회횟수가 적다면 ( 최대 기록이라면, )
                    print("최고기록 갱신~!")        #'최대기록'이라고 알려준다.
                    name=input("\n닉네임을 입력하세요 >> ")       #닉네임 입력받음             
                    names.insert(0,name)    # 이름리스트; 최고 기록이니까 0번째 인덱스에 삽입한다.
                    ranking.insert(0,tryCount)  # 기록리스트; #최고 기록이니까 0번째 인덱스에 삽입한다. #<==================피드백2
                break
            elif tryCount==10 :    #시도횟수를 초과하면 알려주기
                print("입력횟수를 초과하였습니다. 게임오버!")
                break   #<--2주차피드백1
            elif guess>answer:  #정답보다 큰 수를 입력시, 'DOWN'이라고 출력
                print("DOWN")
                max=guess-1       #다음 번 시도에 입력할 숫자 범위를 알려주기 위해, max에 값을 저장한다.
            else:
                print("UP")  #정답보다 작은 수 입력시, 'UP'이라고 출력
                min=guess+1     #다음 번 시도에 입력할 숫자 범위를 알려주기 위해, min에 값을 저장한다.
            tryCount=tryCount+1

    if num==2:  #기록확인     
        count=1 #count변수는 몇 등인지 출력하기 위해 쓰인다.
        print("rank/name/score")
        for n,r in zip(names,ranking):   #기록을 기록한 ranking 리스트를 돌면서, 
            print(str(count) + "등  "+n+"  "+str(r)+"회")  #몇등과 몇회 시도했는지를 출력해준다.
            count=count+1
        print()          

    if num==3 :
         print("즐거운 시간 보내셨나요? 안녕히 가세요^^") # 게임 종료 시, 멘트를 출력해준다. 
         close()    #프로그램 종료전, 게임하는 동안 변경된 리스트내용을 파일에 저장하는 함수
