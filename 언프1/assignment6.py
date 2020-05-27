alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes'

# 1. 한 문장 씩 출력하기 + 줄 바꿈

print("##########################################")
print("#### 1. 한 문장 씩 출력하기 + 줄 바꿈 ####")
print("##########################################\n")

sent_alice = alice.split('. ')
sent_cnt = len(sent_alice)
cnt = 1
for sent in sent_alice:
    print(str(cnt) + '. ' + sent + '.')
    cnt += 1 

# 2. 텍스트 안에 있는 모든 단어를 한 단어 씩 출력하기 + 줄 바꿈

print("\n######################################################################")
print("#### 2. 텍스트 안에 있는 모든 단어를 한 단어 씩 출력하기 + 줄 바꿈 ####")
print("######################################################################\n")

lower_alice = alice.lower()
del_punc_alice = lower_alice.replace(",", '')
del_punc_alice = del_punc_alice.replace('\'', '')
del_punc_alice = del_punc_alice.replace('.', '')
del_punc_alice = del_punc_alice.replace('"', '')
wrd_alice = del_punc_alice.split()
cnt = 1
for word in wrd_alice:
    print(str(cnt) + '. ' + word)
    cnt += 1


# 3. Unique word 뽑고, 각 단어의 빈도수 출력하기 + 줄 바꿈

print("\n##################################################################")
print("#### 3. Unique word 뽑고, 각 단어의 빈도수 출력하기 + 줄 바꿈 ####")
print("##################################################################\n")


unique_word_list = list(set(wrd_alice))
unique_word_list.sort()
cnt = 1
for word in unique_word_list:
    print(str(cnt) + '. ' + word + ': ' + str(wrd_alice.count(word)))
    cnt += 1

# 4. 텍스트를 소문자로 바꾸기 단, 고유명사는 바꾸지 말 것

print("\n#################################################################")
print("#### 4. 텍스트를 소문자로 바꾸기 단, 고유명사는 바꾸지 말 것 ####")
print("#################################################################\n")

## 문자열로 하기

# new_alice = ''
# entity_wrd = ['Alice,', 'White', 'Rabbit']
# for word in alice.split():
#     if word in entity_wrd:
#         new_alice += word + ' '
#     else:
#         low_word = word.lower()
#         new_alice += low_word + ' '

## 리스트로 하기

new_alice = []
entity_wrd = ['Alice,', 'White', 'Rabbit']
for word in alice.split():
    if word in entity_wrd:
        new_alice.append(word)
    else:
        low_word = word.lower()
        new_alice.append(low_word)

new_alice = ' '.join(new_alice)

print(new_alice)
