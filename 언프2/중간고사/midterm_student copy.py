# -*- coding: utf-8 -*-

## 아래 양식을 절대로 수정하지 마세요!!!!

## 학번:
## 이름: 


# 1번
def word_length1(word):
    print(word + ": " + str(len(word)))

def word_length2(word):
    return(word + ": " + str(len(word)))

word = input()

word_length1(word)

print ("1번 문항 결과값", word_length2(word))


# 2번
print ("\n2번 문항 결과값")

def word_extraction(text):
    #<<Body>> 코드 작성 부분
    temp_text = text.lower()
    temp_text = temp_text.replace(".", "")
    words = list(set(temp_text.split()))
    words.sort()
    for i in range(len(words)):
        print(str(i + 1) + ": " + words[i])

text = "Gentleness and kind persuasion win where force and bluster fail."

# <<함수호출>> 코드 작성 부분
word_extraction(text)



# 3번
data = open(r"./언프2/중간고사/per_information.txt", "r", encoding="utf-8").readlines()
names = []
for i in range(0,len(data), 3):
    names.append(data[i])

print ("\n3번 문항 결과값")
with open("./언프2/중간고사/result_per_info.txt", 'w') as file:
    for name in names:
        print(name)
        file.write(name)



# 4번
import re
print ("\n4번 문항 결과값")
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
import operator
print ("\n5번 문항 결과값")
friends_data = open(r"./언프2/중간고사/friends_1_1.txt", "r", encoding="utf-8").read()

# 전처리
friends_data = friends_data.lower()
puncs = ['.', ',', '?', '!', '-', '\'', '\"', ";"]
for punc in puncs:
    friends_data = friends_data.replace(punc, ' ')

def cnt_words(data):
    words = data.split()
    word_list = list(set(words))
    word_list.sort()

    word_dict = {}
    for word in word_list:
        word_dict[word] = words.count(word)

    top_words = tuple(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True))
    return top_words

f_nme = ["monica", 'joey', 'chandler', 'phoebe', "ross", 'rachel']
for name in f_nme:
    text = re.findall(name + r": ([a-z0-9: ]+)", friends_data)
    full_text = '\n'.join(text)
    top_words = cnt_words(full_text)
    print("Top 5 words of {}".format(name.upper()))
    for i in range(0, 5):
        print("{0}: {1}".format(top_words[i][0], top_words[i][-1]))

"""
            word_dict, top_words = cnt_words(sent)
            print("Top 5 words of " + name.upper())
            for i in range(0, 6):
                print("{0}: {1}".format(top_words[i][0], top_words[i][-1]))"""