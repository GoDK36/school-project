alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

#  부호 제거

lower_alice = alice.lower()
del_punc_alice = lower_alice.replace(",", '')
del_punc_alice = del_punc_alice.replace('\'', '')
del_punc_alice = del_punc_alice.replace('.', '')
del_punc_alice = del_punc_alice.replace('"', '')
wrd_alice = del_punc_alice.split()

#  Unique word 뽑고, 각 단어의 빈도수 딕셔너리에 저장하기

unique_word_list = list(set(wrd_alice))
unique_word_list.sort()
cnt = 1
word_cnt = {}
for word in unique_word_list:
    word_cnt[word] = wrd_alice.count(word)

# 단어 입력 받기(소문자로 통일)
inp = input("단어를 입력하세요: ").lower()

if inp in word_cnt.keys():
    print("단어 {0}의 등장횟수는 {1}번입니다".format(str(inp), word_cnt[inp]))
else:
    print("The word you entered is not found")
