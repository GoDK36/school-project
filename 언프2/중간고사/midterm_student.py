# -*- coding: utf-8 -*-

## 아래 양식을 절대로 수정하지 마세요!!!!

## 학번: 201500601
## 이름: 김신우


# 1번
print ("1번 문항 결과값")

# 결과 값이 있는 형태
def word_length1(word):
    print(word + ": " + str(len(word)))

# 결과 값이 없는 형태
def word_length2(word):
    return(word + ": " + str(len(word)))

word = input()  # apple

word_length1(word)

print (word_length2(word))

# 2번
print ("\n2번 문항 결과값")

def word_extraction(text):
    #<<Body>> 코드 작성 부분
    # 소문자화
    temp_text = text.lower()
    # 문장기호 삭제
    temp_text = temp_text.replace(".", "")
    # 중복단어 제거
    words = list(set(temp_text.split()))
    # 알파벳 순서로 정리
    words.sort()
    for i in range(len(words)):
        print(str(i + 1) + ": " + words[i])

text = "Gentleness and kind persuasion win where force and bluster fail."

#<<함수호출>> 코드 작성 부분
word_extraction(text)


# 3번
print ("\n3번 문항 결과값")

# 상대경로로 파일 열기
data = open(r"./언프2/중간고사/per_information.txt", "r", encoding="utf-8").readlines()
# 이름만 리스트에 저장하기
names = []
for i in range(0,len(data), 3):
    names.append(data[i].replace("\n", ''))

# 이름만 텍스트 파일로 저장하기
with open("./언프2/중간고사/result_per_info.txt", 'w') as file:
    for name in names:
        # 콘솔창에 출력
        print(name)
        file.write(name + "\n")


# 4번
print ("\n4번 문항 결과값")

import re

# 데이터 불러오기
aesop_data = open(r"./언프2/중간고사/Aesop_001_Task2_009.TextGrid.utf16", "r", encoding="utf-16").read()
# 텍스트만 추출하기
words = re.findall(r'text= \"([a-zA-Z<>?\/]+)\"', aesop_data)
# 단어 시작점과 끝점 안덱스 파악
start_idx = words.index("<s>")
end_idx = words.index("</s>")
# 단어로만 리스트 만들기
word = []
for i in range(start_idx+1, end_idx):
    word.append(words[i])
# sp 제거하고 결과 추출
print(' '.join(word).replace('sp', '').replace('  ', ' '))



# 5번 
print ("\n5번 문항 결과값")

import operator

# 데이터 불러오기
friends_data = open(r"./언프2/중간고사/friends_1_1.txt", "r", encoding="utf-8").read()

# 전처리
# 소문자화
friends_data = friends_data.lower()
# 문장부호 제거
puncs = ['.', ',', '?', '!', '-', '\'', '\"', ";"]
for punc in puncs:
    friends_data = friends_data.replace(punc, ' ')

# 단어 빈도 세는 함수
def cnt_words(data):
    words = data.split()
    word_list = list(set(words))
    word_list.sort()

    word_dict = {}
    for word in word_list:
        word_dict[word] = words.count(word)

    # 딕셔너리 sorting
    top_words = tuple(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True))

    return top_words

# 등장인물 이름
f_nme = ["monica", 'joey', 'chandler', 'phoebe', "ross", 'rachel']
for name in f_nme:
    # 등장인물의 발화만 찾는 정규식
    text = re.findall(name + r": ([a-z0-9: ]+)", friends_data)  # 중간에 시간표현이 있어 숫자도 포함
    full_text = '\n'.join(text)
    top_words = cnt_words(full_text)
    print("Top 5 words of {}".format(name.upper()))
    for i in range(0, 5):
        print("{0}: {1}".format(top_words[i][0], top_words[i][-1]))