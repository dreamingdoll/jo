
# 신촌날씨 온도 출력

import urllib.request as ur

from bs4 import BeautifulSoup as bs # html 언어 읽어주는 함수
import urllib

지역 = input("지역 : ")
검색어 = urllib.parse.quote(지역 + '날씨')
주소 = 'https://search.naver.com/search.naver?ie=utf8&query=' + 검색어
웹문서 = ur.urlopen(주소)
soup = bs(웹문서.read(), 'html.parser')
온도 = soup.find_all('span', {"class" : "todaytemp"})

print(f"현재 {지역}의 온도는 : {온도[0].text}도 입니다")

미세먼지 = soup.find_all('dd', {"class" : "lv1"})
print(f"현재 {지역}의 미세먼지 : {미세먼지[0].text} 입니다")

오존지수 = soup.find_all('dd', {"class" : "lv2"})
print(f"현재 {지역}의 오존지수 : {오존지수[0].text} 입니다")

