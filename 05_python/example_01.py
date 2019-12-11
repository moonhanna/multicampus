import requests
import webbrowser
from bs4 import BeautifulSoup

# webbrowser.open('www.google.com')
# webbrowser.open_new('www.naver.com')
# webbrowser.open_new_tab('www.daum.net')


# res = requests.get('http://apple.kr')
# # print(res)
# # print(res.text) #주소안의 모든 텍스트가 나타난다. 
# print(res.status_code) #200번(서버가정상일때)이 나오는지 확인하기 위한 코드 (404나오는지 확인하는 ) -->상태정보만확인
# print(res.text)


url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
soup = BeautifulSoup(response,'html.parser')
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)