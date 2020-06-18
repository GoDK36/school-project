print("####################################")
print("####### 3-1 data 변수에 담기 #######")
print("####################################")
print()

def OpenData(file_path):
    with open(file_path, "r") as f1:
        data = f1.read()
    return data

# Obama_speech 파일 경로
path = "E:\Develop\python\school-project\언프1\기말\Obama_speech.txt"

data = OpenData(path)
print(data)

#############################################################################

print()
print("###################################")
print("######## 3-2 데이터 전처리 ########")
print("###################################")
print()

def DelPunc(data):
    # 문장부호 제거
    del_punc_data = data.replace('.', '')
    del_punc_data = del_punc_data.replace('--', '')
    del_punc_data = del_punc_data.replace(';', '')
    del_punc_data = del_punc_data.replace(':', '')
    del_punc_data = del_punc_data.replace('(', '')
    del_punc_data = del_punc_data.replace(')', '')
    del_punc_data = del_punc_data.replace('?', '')
    del_punc_data = del_punc_data.replace(',', '')
    del_punc_data = del_punc_data.replace('"', '')

    return(del_punc_data)

del_punc_data = DelPunc(data)

print(del_punc_data)

#############################################################################

print()
print("######################################")
print("######## 3-3 인칭 대명사 횟수 ########")
print("######################################")
print()

def Person(data):
    # 전처리
    data = DelPunc(data)
    # 단어 리스트화
    word_list = data.split()

    # 1인칭 리스트
    first_person = ['I', 'my', 'me', 'mine']
    # 3인칭 리스트
    third_person = ['we', 'our', 'us', 'ours']

    first_cnt = 0
    third_cnt = 0
    for word in word_list:
        # 1인칭 횟수 세기
        for first in first_person:
            if word.lower() == first.lower():
                first_cnt += 1
        # 3인칭 횟수 세기
        for third in third_person:
            if word.lower() == third.lower():
                third_cnt += 1

    return first_cnt, third_cnt

first_cnt, third_cnt = Person(data)

print("1인칭 사용횟수: {0}\n3인칭 사용횟수: {1}".format(first_cnt, third_cnt))

#############################################################################

print()
print("##################################")
print("######## 3-4 가장 긴 단어 ########")
print("##################################")
print()

def LongWord(data):
    # 전처리
    data = DelPunc(data)

    # 단어 리스트화
    word_list = data.split()

    # 단어 길이들 리스트화
    len_word = []
    for word in word_list:
        len_word.append(len(word))

    # 두 리스트의 인덱스가 같다는 튿성을 이용, len_word에서 제일 큰 숫자의 인덱스 뽑기
    long_wrd_idx = len_word.index(max(len_word))

    return(word_list[long_wrd_idx])

long_word = LongWord(data)

print(long_word)