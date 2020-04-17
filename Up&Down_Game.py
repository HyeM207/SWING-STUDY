import random  #랜덤으로 수를 만들기 위해 random 라이브러리 추가
num=0  #시작화면 입력받는 변수로  while문에 쓰이는데, while문 돌기 위해 미리 초기화 
ranking = []  #게임 기록 저장할 빈 리스트

while num!=3:   # 숫자 3 입력시, 게임 종료하기
    guess=0  #=사용자 입력받는 변수
    answer=random.randrange(1,101)  # 정답은 random의 randrange함수를 이용해, 1~100까지의 난수를 while돌때 마다 갱신한다.
    max=100 #게임할 때,입력할 최대값을 알려주는 변수
    min=1   #게임할 때,입력할 최소값을 알려주는 변수
   # print("\nanswer : "+str(answer))  // 
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    num=int(input(">> "))   #무엇을 할지 입력받는다.
    if num==1:    #게임시작
        for i in range (1,11):  # 게임가능한 최대 기회는 10번
            guess=int(input(str(i)+ "번째 숫자입력(" +str(min)+ "~" +str(max) + ") : ")) #guess변수에 추측한 값이 들어간다.
            if guess>max or guess<min :  #만약, 범위에서 벗어난 값 입력시, 메시지 출력
                print("범위에 벗어난 값을 입력하였습니다. 범위에 맞게 입력해주세요.")                
            elif guess==answer :    #만약 정답이라면,
                print("정답입니다!!\n"+str(i)+"번만에 맞추셨습니다") # 정답이라 알려주기.
                if len(ranking)==0 or ranking[0] > i:   #만약, 기록 최대값이 들어간 0번째 값보다 기회횟수가 적다면 ( 최대 기록이라면, )
                    print("최고기록 갱신~!")        #'최대기록'이라고 알려준다.
                    ranking.append(i)   # ranking 리스트에 기록을 해준다.
                    ranking.sort()      #다음 기록저장&확인을 위해, sort함수를 이용해 오름차순으로 정렬을 해준다. 
                break
            elif i==10 :    #시도횟수를 초과하면 알려주기
                print("입력횟수를 초과하였습니다. 게임오버!")
            elif guess>answer:  #정답보다 큰 수를 입력시, 'DOWN'이라고 출력
                print("DOWN")
                max=guess       #다음 번 시도에 입력할 숫자 범위를 알려주기 위해, max에 값을 저장한다.
            else:
                print("UP")  #정답보다 작은 수 입력시, 'UP'이라고 출력
                min=guess      #다음 번 시도에 입력할 숫자 범위를 알려주기 위해, min에 값을 저장한다.
        
    if num==2:  #기록확인     
        count=1 #count변수는 몇 등인지 출력하기 위해 쓰인다.
        for i in ranking:   #기록을 기록한 ranking 리스트를 돌면서, 
            print(str(count) + "등 : "+str(i)+"회")  #몇등과 몇회 시도했는지를 출력해준다.
            count=count+1
        print()           
print("즐거운 시간 보내셨나요? 안녕히 가세요^^") # 게임 종료 시, 멘트를 출력해준다. 