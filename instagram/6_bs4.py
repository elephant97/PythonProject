import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) #처음으로 발견된 title 태그를 갖고와라
# print(soup.title.get_text()) #처음으로 발견된 title 태그를 텍스트 형태로 갖고와라
# print(soup.a) # soup객체에서 처음으로 발견된 a element를 갖고와라
# print(soup.a.attrs) # a element의 가 가지고있는 속성 정보 가져오기
# print(soup.a["href"]) # a element의 herf 속성 값 출력

#가져오려는 페이지를 잘 알지 못할 때 

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) #attrs 속성값 조건에 맞는 a 태그에 해당하는 첫번째 element를 가져옴
# print(soup.find(attrs={"class":"Nbtn_upload"})) #class가 Nbtn인 어떤 element를 찾아줘
# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.get_text())
# rank2 = rank3.previous_sibling.previous_sibling #불러온 정보의 이전 태그 정보를 찾기
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li") #li의 그 다음 태그 정보를 찾기
# print(rank3.a.get_text())
# print(rank1.find_next_siblings) #li의 그 다음 태그 정보'들'을 찾기

webtoon = soup.find("a", text="내가 죽기로 결심한 것은-23화") #<a>태그 사이에 있는 이정보를 이용하여 찾기</a>
print(webtoon)