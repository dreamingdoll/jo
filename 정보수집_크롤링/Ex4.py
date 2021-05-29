import urllib.request as ur

from bs4 import BeautifulSoup as bs # html 언어 읽어주는 함수
import urllib
while True:
    모델 = input("모델 : ")
    if 모델 == "종료":
        break
    검색어 = urllib.parse.quote(모델 + '가격')
    주소 = 'https://search.naver.com/search.naver?ie=utf8&query=' + 검색어
    웹문서 = ur.urlopen(주소)
    soup = bs(웹문서.read(), 'html.parser')
    가격 = soup.find_all('span', {"class": "property"})
    찾는문자 = "판매"
    for i in 가격:
        b = 찾는문자 in i.text
        if b:
            print(f"{모델}의 출시가 : {가격[0].text}")


