from bs4 import BeautifulSoup  
import urllib.request
import os
import re  #re.sub을 위해 모듈 추가

#01.해당 웹툰 HTML 파싱하기 
html = urllib.request.urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=715772&weekday=thu") 
result = BeautifulSoup(html.read(),"html.parser") 

#02. 웹툰이름 필터링 하기
webtoonName = result.findAll("h2")
webtoonName=str(webtoonName[1])
webtoonName = re.sub('<span.*?>.*?</span>', '', webtoonName, 0, re.I|re.S) #span 태그 제거
webtoonName =re.sub('<.+?>','',webtoonName) # h2 태그 제거
webtoonName=re.sub('| |\n|\t','',webtoonName) # 공백, 엔터, 탭키 제거

#03. 웹툰 파일명 만들기
os.mkdir(webtoonName)
os.chdir("C:/Users/김혜민/Desktop/python 코드/%s"%(webtoonName))
print(webtoonName+" folder created successfully")


#04. 회차별 이름 필터링 하기
titles=result.findAll("td",{"class":"title"})

for t in titles:
    title=str(t.find("a").text) 
    #5. 회차 파일 만들기
    os.mkdir("C:/Users/김혜민/Desktop/python 코드/%s/%s"%(webtoonName,title)) #회차 파일 만들기
    os.chdir("C:/Users/김혜민/Desktop/python 코드/%s/%s"%(webtoonName,title)) #회차 파일로 이동
    

    #6. 이미지 다운받기 
    htmlTitle= urllib.request.urlopen("https://comic.naver.com"+t.find("a")['href']) # 회차별 만화로 이동
    result2= BeautifulSoup(htmlTitle.read(),"html.parser") # 코드가져오기
    img = result2.find("div",{"class":"wt_viewer"})#필터링 _본문 내용만
    
    i=1 # 해당 회차의 이미지 저장을 위한 변수 (ex. 1.jpg, 2.jpg, 3.jpg)
    for s in img.findAll("img"): #이미지 하나씩 처리하기 위해서
        url=s.get("src") #이미지 다운받는 링크
        path="C:/Users/김혜민/Desktop/python 코드/%s/%s"%(webtoonName,title) #경로 설정
        name=str(i)+".jpg" #파일이름.확장자
        save=path+"/"+name  
        
        #우회하기 위한 코드
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        

        urllib.request.urlretrieve(url,save) #이미지 다운로드
        i=i+1

    print(title + "\tsaved completely!") 


