alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

# 1. 문장 부호 제거하기
low_alice = alice.lower()

## NE(Named Entity) 살리기
# 정규표현식 사용
# ne = re.compile("[A-Z]{1}[a-zA-Z]*(\s[A-Z]{1}[a-zA-Z]*)*")      # 이런 방식이면 New York, Shin Woo Kim 도 잡을 수 있을거 같습니다...?

# 라이브러리 사용(nltk, kiwi, soynlp와 같은 형태소 분석기) 후 tag 정보를 바탕으로 regex 사용...?

# 개체명 관련해서 blink라는 페이스북에서 개발한 모듈도 등장했다고 합니다
# 위키피디아를 이용해서 개체명을 파악하고 해당 정보를 넘겨준답니다!
# https://github.com/facebookresearch/BLINK
# 설치 오류로 아직 사용 못해봤습니다...ㅜ



del_punc_alice = low_alice.replace(",", '')
del_punc_alice = del_punc_alice.replace('\'', '')
del_punc_alice = del_punc_alice.replace('.', '')
del_punc_alice = del_punc_alice.replace('"', '')

print("####################################")
print("##### 1. 문장 부호 제거한 alice #####")
print("####################################")
print('\n', del_punc_alice, "\n")


# 2. 띄어쓰기 단위로 분할하기

sep_alice = del_punc_alice.split()

print("####################################")
print("###### 2. 띄어쓰기 분할 alice ######")
print("####################################")
print('\n', sep_alice, "\n")


# 3. unique word list 만들기

unique_word_list = list(set(sep_alice))


print("####################################")
print("#### 3. unique word list 만들기 ####")
print("####################################")
print('\n', unique_word_list, '\n')


# 4. 3의 목록을 오름차순으로 정렬

unique_word_list.sort()

print("########################################")
print("#### 4. 3의 목록을 오름차순으로 정렬 ####")
print("########################################")
print('\n', unique_word_list, '\n')

# 4-2. 3의 목록을 내림차순으로 정렬

unique_word_list.sort(reverse=True) 

print("########################################")
print("### 4-2. 3의 목록을 내림차순으로 정렬 ###")
print("########################################")
print('\n', unique_word_list, '\n')

# 5. 문장 단위로 분할하기

sent_alice = alice.split('.')       # 하지만 이런 방식은 ?나 ! 등의 부호로 끝나는 경우를 캐치하지 못할 듯합니다...

print("########################################")
print("######## 5. 문장 단위로 분할하기 ########")
print("########################################")
print('\n', sent_alice, '\n')

# 6. "the", "on","of", "she" 가 몇 번 등장하는지 구하고 , freq 라는 딕셔너리를 만들어 단어와 등장 횟수를 담기

freq = {'the':sep_alice.count("the"), 'on':sep_alice.count('on'), 'of':sep_alice.count('of'), 'she':sep_alice.count('she')}

print("########################################")
print("######## 6. freq 딕셔너리 만들기 ########")
print("########################################")
print('\n', freq, '\n')

# 7. 0 번 인덱스에서 부터 8 번까지의 단어의 길이를 구하고 num_letter라는 딕셔너리를 만들어 단어와 단어 길이 담기


# 최종 unique_word_list 가 내림차순이었어가지고 year부터 시작합니다!
num_letter = { 
    unique_word_list[0]:len(unique_word_list[0]),
    unique_word_list[1]:len(unique_word_list[1]),
    unique_word_list[2]:len(unique_word_list[2]),
    unique_word_list[3]:len(unique_word_list[3]),
    unique_word_list[4]:len(unique_word_list[4]),
    unique_word_list[5]:len(unique_word_list[5]),
    unique_word_list[6]:len(unique_word_list[6]),
    unique_word_list[7]:len(unique_word_list[7]),
    unique_word_list[8]:len(unique_word_list[8])
    }

print("########################################")
print("##### 7. num_letter 딕셔너리 만들기 #####")
print("########################################")
print('\n', num_letter, '\n')



