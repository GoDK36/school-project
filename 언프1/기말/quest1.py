print("##############################")
print("####### 1-1 홀수 짝수? #######")
print("##############################")
print()

num = int(input("숫자를 입력하세요: "))
if num % 2 == 0:
    print("입력한 숫자는 짝수입니다.")
else:
    print("입력한 숫자는 홀수입니다.")

#############################################################################

print()
print("#####################################")
print("######## 1-2 문자열 슬라이싱 ########")
print("#####################################")
print()

a = "It was fantastic"

print("방법1: ", a[-9:])
print("방법2: ", a[7:])

#############################################################################

print()
print("###################################")
print("######## 1-3 단어 딕셔너리 ########")
print("###################################")
print()

words = ["placement", 'neutral', 'attracting', 'effect', 'delivery']

word_dict = {}
for word in words:
    word_dict[word] = len(word)
    # print("The length of the word " + '"' + word + '" is ' + str(len(word)))도 가능하지만 교수님 의도가 딕셔너리를 응용하는거 같아 아래에 작성합니다.

for word, length in word_dict.items():
    print("The length of the word " + '"' + word + '" is ' + str(length))

#############################################################################

print()
print("#################################")
print("######## 1-4 문자열 조작 ########")
print("#################################")
print()

data = "The new coronavirus's link to a market in China is the latest example of an infection that likely spread from animals to people."

# 소문자 제거

low_data = data.lower()

# 문장부호 제거

del_punc_data = low_data.replace('.', '')
del_punc_data = del_punc_data.replace('\'', '')

# 단어로 나누어 리스트로 담기

word_list = del_punc_data.split()

# 재결합하기

re_data = ' '.join(word_list)

# 전체 단어 수 세기

word_len = len(word_list)

# unique word 오름차순 정렬하기

unique_word = list(set(word_list))
unique_word.sort()
