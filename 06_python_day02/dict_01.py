# Dictionary 만드는 방법 - 3가지
# 1. 
my_dict = {'한국어':'안녕', '영어':'hi', '독일어':'Guten tag'}
# print(my_dict)
# 2. 
my_dict = {}
my_dict['한국어']='안녕'
my_dict['영어']='hi'
my_dict['독일어']='Guten tag'
# print(my_dict)
# 3.
my_dict = dict(한국어='안녕', 영어='hi', 독일어='Guten tag')
# print(my_dict)

area_code = {
    '서울':'02'
}
area_code['경기도']='031'

# print(area_code)

# for key in area_code:
#     print(key)
#     print(area_code[key])
    
# .items()
# for key, value in area_code.items():
#     print(key, value)
    
# # value만 가져오기
# for value in area_code.values():
#     print(value)
    
# # key 가져오기
# for key in area_code.keys():
#     print(key)

'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('=========== Q1 ===========')

sum_score = 0

for s in score.values():
     sum_score += s
result = sum_score / len(score) 
print(result)


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 84,
        '국어': 90,
        '음악': 92
    },
    'b': {
        '수학': 83,
        '국어': 91,
        '음악': 77
    }
}

# 아래에 코드를 작성해 주세요.
print('=========== Q2 ===========')

sum_score = 0
count = 0 

for person_score in scores.values():
    for subject_score in person_score.values():
         sum_score += subject_score
         count += 1

result = sum_score / count
print(result)


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?
print('========== Q3-1 ==========')
for key, value in city.items():
    temps = 0
    for t in value:
        temps += t
    temp = temps / len(value)
    print(f'{key}: {temp}')

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
print('========== Q3-2 ==========')
count = 0
for key, value in city.items():
    #최초 시행시에만 적용되는 조건문
    if count == 0:
        hot_temp = max(value)
        cold_temp = min(value)
        hot_city = key
        cold_city = key
        count += 1
    else:
        if max(value) > hot_temp:
            hot_temp = max(value)
            hot_city = key
        if min(value) < cold_temp:
            cold_temp = min(value)
            cold_city = key

print(f'가장 추웠던 곳은 {cold_city},{cold_temp}도 였고 가장 더웠던 곳은 {hot_city},{hot_temp}도 입니다.')

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
print('========== Q3-3 ==========')
if 2 in city['서울']:
    print('있습니다.')
else:
    print('없습니다.')

# 아래에 코드를 작성해 주세요.