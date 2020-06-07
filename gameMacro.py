from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/김혜민/Desktop/python 코드/chromedriver')
driver.get('http://zzzscore.com/1to50/?ts=1591119734908#')

l=[] #실행 리스트1 (1~25까지 실행할 버튼의 xpath)
count=[] #실행 리스트1의 버튼들의 인덱스 저장
c=1  # 몇번째 숫자의 버튼인지 카운트

#### 01. 1~25까지의 숫자 버튼들의 인덱스와, xpath경로를 저장 (순서대로)
while c<26:  #1~25까지 버튼 
        for p in range(1,26): # 1~25인덱스의 버튼들 중, 순서에 맞는 버튼 선택 
                    btn =driver.find_element_by_xpath('//*[@id="grid"]/div['+str(p)+']')
                    if btn.text == str(c):
                        btn =driver.find_element_by_xpath('//*[@id="grid"]/div['+str(p)+']/span')
                        l.append(btn)
                        count.append(p)
                        c=c+1
                        break


#### 02. 1~25 버튼 클릭(게임시작) + 클릭한 버튼들의 변환 값을 딕셔너리에 저장
l2={} #실행 딕셔너리 2 _키: 누를 버튼  , 값 : xpath

for k in range(0,25): #미리 정렬해둔 리스트에서 뽑아, 1~25버튼을 클릭함 + 이와 동시에, 클릭한 그 블록의 바뀐 숫자를 기록함. 
        exe=l[k]
        exe.click()  #1~25버튼 클릭
        time.sleep(0.104)   #클릭 후, 블럭 바뀌는 거 기다리기 위해서 기다림
        c=count[k]   #위에서 클릭한 버튼의 위치를 뽑아옴.
        btn2 =driver.find_element_by_xpath('//*[@id="grid"]/div['+str(c)+']')  
        btn3 =driver.find_element_by_xpath('//*[@id="grid"]/div['+str(c)+']/span')  
        l2[str(btn2.text)]=btn3 #키(인덱스)에는 숫자값을, 값에는 실행문(xpath) 를 넣는다.   


#### 03. 26~50까지의 버튼 클릭
for k in sorted(l2):  #키 값을 기준으로 정렬하여,
    exe=l2[k] #값을 가져와
    exe.click() #실행한다. 