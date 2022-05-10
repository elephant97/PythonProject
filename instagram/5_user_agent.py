from email import header
import requests

url = "https://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"}

#res = requests.get("https://www.instagram.com/petprincess_korea/")
res = requests.get(url, headers=headers)
res.raise_for_status() #오류가 생겼을 때 실행하지 못하게 처리함
print("웹 스크래핑을 진행합니다.")
#if res.status_code == requests.codes.ok: #200 이상이면 정상
#    print("정상입니다")
#else:
#    print("문제가 생겼습니다. [에러코드: ",res.status_code)
    
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)    