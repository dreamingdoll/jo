
# API : 미리 만들어둔 코드[ 프로그램 ]
    # 네이버 API

# 1. 네이버 로그인
# 2. 네이버 API 검색 => 네이버 개발자 센터
# 3. 사이드 메튜에서 어플리케이션 등록
    # 1. 어플리케이션 이름 : 아무거나 넣기[ 파이썬입시 ]
    # 2. 사용 api : 검색
    # 3. 서비스 환경 WEB => RUL : http://python.com

# 4. 사이트 메뉴 => Documents
# 5. 검색 결과는 딕셔너리에 호출된다[ 딕셔너리 데이터 가공 ]




# 발급받은 어플리케이션 정보를 변수에 저장
import re

Client_ID = 'NLnc9EHjALeGCtAsL07I'
Client_Secret = 'iDl54xUzh5'

import os
import sys
import urllib.request
import json
client_id = Client_ID
client_secret = Client_Secret

# 블로그

search_word = input("블로그 검색 : ")
encText = urllib.parse.quote(search_word)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    search_result = response_body.decode('utf-8') # utf-8 : 한글지원

    # 검색결과 가공하기
    json_result = json.loads(search_result)

    search_result_list = [    ]
    for i in json_result['items']:
        title = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print(title)

else:
    print("Error Code:" + rescode)


# 책

search_word = input("책 검색 : ")
encText = urllib.parse.quote(search_word)
url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


# 뉴스

search_word = input("뉴스 검색 : ")
encText = urllib.parse.quote(search_word)
url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)