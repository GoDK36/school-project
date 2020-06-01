## alice.txt 파일을 열고 읽기

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

# alice_word_list.txt에 저장

file2 = open("alice_word_list.txt", "w")

print("\n#################################")
print("#### 알파벳 순으로 단어 출력 ####")
print("#################################\n")

for word in unique_word_list:
    # 화면에 출력
    print(word)
    file2.write(word + '\n')

print("\n#############################")
print("#### unique 단어 수 출력 ####")
print("#############################\n")
print("The number of words in the data is " + str(len(unique_word_list)))

file2.write("The number of words in the data is " + str(len(unique_word_list)))
file2.close()

# "단어: 빈도"로 되있는 딕셔너리 줄바꿈해서 출력 및 저장

file3 = open("alice_freq.txt", "w")

print("\n###########################")
print("#### 단어: 빈도로 출력 ####")
print("###########################\n")

for word, freq in alice_dict.items():
    # 화면에 출력
    print(word + ': ' + str(freq))
    
    # alice_freq.txt 에 저장
    file3.write(word + ': ' + str(freq) + '\n')

file3.close()