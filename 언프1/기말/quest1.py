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

print()
print("###################################")
print("######## 1-4-a 소문자 제거 ########")
print("###################################")
print()

low_data = data.lower()

print(low_data)

print()
print("#####################################")
print("######## 1-4-b 문장부호 제거 ########")
print("#####################################")
print()

del_punc_data = low_data.replace('.', '')
del_punc_data = del_punc_data.replace('\'', '')

print(del_punc_data)

print()
print("####################################################")
print("######## 1-4-c 단어 리스트에 담고 재결합하기 ########")
print("####################################################")
print()

word_list = del_punc_data.split()

print("단어 리스트\n", word_list, '\n')

# 재결합하기

re_data = ' '.join(word_list)

print("재결합\n", re_data)

print()
print("####################################")
print("######## 1-4-d 단어 수 세기 ########")
print("####################################")
print()

word_len = len(word_list)

print(word_len)

print()
print("####################################################")
print("######## 1-4-e unique word 오름차순 정렬하기 ########")
print("####################################################")
print()

unique_word = list(set(word_list))
unique_word.sort()

print(unique_word)