from bs4 import BeautifulSoup  
import urllib.request

# 해당사이트에서 html형식으로 리소스를 읽어온다.
html = urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html") 
result = BeautifulSoup(html.read(),"html.parser")   
# 함수를 이용해서, a링크만 추출한다.
department = result.findAll("a")

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***")
print("학과\t\t\t홈페이지")

for s in department:
   
   # 아래의 단어는 필터링 해준다.
    if s.text =="공동기기실"or s.text=="자율전공학부" :
            continue
    if "대학원" in s.text or "교육원" in s.text:
            continue
    
    # 그 외에는 해당 사이트로 들어가, 리소스를 읽어온다.
    # 이때, major 변수에는 a링크에서 특정 클래스(링크버튼에 해당됨)를 만족하는 경우에만 저장한다. 
    else:   
        htmlDeeper= urllib.request.urlopen("http://www.swu.ac.kr"+s['href'])    #홈페이지 불러오기
        result2= BeautifulSoup(htmlDeeper.read(),"html.parser")         #html 형식으로 바꿔주기
        major = result2.find("a",{"class","btn btn_xl btn_blue_gray"}) # 필터링 하여 가져옴 ( 특징이 class는 저걸로 되어있었음)
      
        print(s.text,end='') #학과 이름 출력
        # 컴퓨터학과 같은 경우에는 None이여서, if문으로 걸러주지 않으면 에러이므로 따로 빼준다.
        if major is None : 
            print("\t\t홈페이지가 존재하지 않음")
        else:
            if "홈페이지" in major.text:    # 하단의 버튼 중 '홈페이지'버튼만 링크를 출력해준다.
                print("\t\t"+major['href'])
            else :   # 그 외의 경우는 홈페이지 존재하지 않음으로 판단
                print("\t\t홈페이지가 존재하지 않음")
   


