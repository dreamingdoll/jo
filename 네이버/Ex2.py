
# 네이버 검색 API를 이용한 JSON 가공 프로그램
    # JSON : 키-값 => 한쌍 <--- 딕셔너리와 유사

import os
import sys
import urllib.request
import json
import re


def search_naver(category, search_result_num):
    client_id = 'NLnc9EHjALeGCtAsL07I'
    client_secret = 'iDl54xUzh5'
    url = "https://openapi.naver.com/v1/search/" + category +".json"
    option = "&display="+search_result_num+"&sort=count"
    query = "?query="+urllib.parse.quote(input(category+"의 검색 정보 입력 : "))
    url_query = url + query + option

    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    search_result = response_body.decode('utf-8')  # utf-8 : 한글지원

    # 검색결과 가공하기
    json_result = json.loads(search_result)

    for i in json_result['items']:
        title = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print("---> 검색결과 : "+ title)

        if category == "shop":
            print("------> 최저가 :", i['lprice'])

        if category == "movie":
            print("------> 평점 :", i['userRating'])

        if category == "news":
            print("------> 주요내용 :", i['description'])


while True: # 무한 반복 : 0 을 입력하면 종료

    print("검색[naverAPI] 프로그램")
    print("카테고리[1.뉴스 2.쇼핑 3.도서 4.영화 5.백과사전 ] 0.종료")
    choice = int(input(("선택 : "))) # 입력받아 choice(선택) 변수에 저장

    if choice == 1:
        category = 'news'
        search_result_num = input("뉴스 선택 했습니다. 몇개 출력할까요? : ")
        search_naver(category, search_result_num)

    if choice == 2:
        category = 'shop'
        search_result_num = input("쇼핑 선택 했습니다. 몇개 출력할까요? : ")
        search_naver(category, search_result_num)

    if choice == 3:
        category = 'book'
        search_result_num = input("도서 선택 했습니다. 몇개 출력할까요? : ")
        search_naver(category, search_result_num)

    if choice == 4:
        category = 'movie'
        search_result_num = input("영화 선택 했습니다. 몇개 출력할까요? : ")
        search_naver(category, search_result_num)

    if choice == 5:
        category = 'encyc'
        search_result_num = input("백과사전 선택 했습니다. 몇개 출력할까요? : ")
        search_naver(category, search_result_num)

    if choice == 0:
        print("---> 이용해주셔서 감사합니다.")
        break # 반복문 종료


