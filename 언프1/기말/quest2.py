import re

print("######################################")
print("####### 2-1 단어-품사 딕셔너리 #######")
print("######################################")
print()

with open(r"E:\Develop\python\school-project\언프1\기말\wsj_partial.txt", "r") as f1:
    text = f1.read()

word_pat = re.compile(r"(\w+)/")
pos_pat = re.compile(r"/(\w+)")

words = word_pat.findall(text)
poses = pos_pat.findall(text)

word_dict = {}
for word, pos in zip(words, poses):
    word_dict[word] = pos

print(word_dict)

#############################################################################

print()
print("############################################")
print("######## 2-2 활용형 원형으로 바꾸기 ########")
print("############################################")
print()

lemma_dict = {}
for word, pos in word_dict.items():
    # 복수 명사
    if pos == 'NNS':
        lemma = word[:-1]
        lemma_dict[lemma] = 'NN'

    # 과거 분사
    elif pos == 'VBN':
        lemma = word[:-1]
        lemma_dict[lemma] = 'VB'

    # 현재 분사
    elif pos == 'VBG':
        lemma = word[:-3] +'e'
        lemma_dict[lemma] = 'VB'

    # 과거시제
    elif pos == 'VBD':
        if word[-2] == 'i':
            lemma = word[:-2] + 'y'
            lemma_dict[lemma] = 'VB'
        else:
            lemma = word[:-2]
            lemma_dict[lemma] = 'VB'

    # 1,2인칭 단수
    elif pos == 'VBP':
        lemma = word
        lemma_dict[lemma] = 'VB'

    # 3인칭 단수
    elif pos == 'VBZ':                      
        lemma = word[:-1]
        if lemma == 'ha':
            lemma = lemma + 've'
            lemma_dict[lemma] = 'VB'
        elif lemma == 'i':
            lemma = 'be'
            lemma_dict[lemma] = 'VB'
        else:
            lemma_dict[lemma] = 'VB'
    else:
        lemma_dict[word] = pos

print(lemma_dict)

#############################################################################

print()
print("########################################")
print("######## 2-3 dic.txt로 저장하기 ########")
print("########################################")
print()

file = open("dic.txt", "w")

for word, pos in sorted(lemma_dict.items()):
    file.write(word + ': ' + pos + '\n')

file.close()

#############################################################################

print()
print("###########################################")
print("######## 2-4 명사 & 동사 단어 목록 ########")
print("###########################################")
print()

nouns = []
verbs = []
for word, pos in lemma_dict.items():
    if pos in 'NN':
        nouns.append(word)
    elif pos in 'VB':
        verbs.append(word)

print("nouns: ", nouns)
print("verbs: ", verbs)