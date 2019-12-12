import requests
import random
 
URL_GetLottoNumber = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=888"
resp = requests.get(URL_GetLottoNumber)
lotto = resp.json()

winner = []
for i in range(1,7):
    winner.append(lotto[f'drwtNo{i}'])
print(winner)

numbers = sorted(random.sample(range(1,46),6))
print(numbers)

matched = 0
for num in numbers:
    if num in winner:
        matched += 1

cnt = 0
while matched < 4:
    numbers = sorted(random.sample(range(1,46),6))
    matched = 0
    for num in numbers:
        if num in winner:
            matched += 1
    cnt += 1
    print(cnt)
    print(winner)
    print(numbers)

    if matched == 6:
        print('1등')
    elif matched == 5:
        if lotto['bnusNo'] in numbers:
            print('2등')
        else:
            print('3등')
    elif matched == 4:
        print('4등')
    elif matched == 3:
        print('5등')
    else:
        print('꽝')