## alice.txt 파일을 열고 읽어서
##
## -기호 모두 삭제
##
## -모두 소문자로 바꾸기
##
## -각 단어의 빈도 세고, 딕셔너리 형태로 저장하기(예: “apple”: 3)

file = open(r"E:\Develop\python\school-project\언프1\alice.txt", "r")
alice = file.read()

# 소문자화
lower_alice = alice.lower()

#기호 모두 삭제
del_punc_alice = lower_alice.replace(",", '')
del_punc_alice = del_punc_alice.replace('\'', '')
del_punc_alice = del_punc_alice.replace('.', '')
del_punc_alice = del_punc_alice.replace('"', '')
wrd_alice = del_punc_alice.split()

# unique word 만들기
unique_word_list = list(set(wrd_alice))
unique_word_list.sort()

# 딕셔너리 만들기
alice_dict = {}
for word in unique_word_list:
    alice_dict[word] = wrd_alice.count(word)

# 알파벳 순으로 단어 출력

print("\n#################################")
print("#### 알파벳 순으로 단어 출력 ####")
print("#################################\n")
print(unique_word_list)

# unique 단어 수 출력

print("\n#############################")
print("#### unique 단어 수 출력 ####")
print("#############################\n")
print("The number of words in the data is " + str(len(unique_word_list)))

# alice_word_list.txt에 저장

file2 = open("alice_word_list.txt", "w")
file2.write(unique_word_list, "'\n'The number of words in the data is " + str(len(unique_word_list)))

# "단어: 빈도"로 되있는 딕셔너리 줄바꿈해서 출력

# alice_freq.txt 에 저장