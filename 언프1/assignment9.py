import re

with open(r"E:\Develop\python\school-project\언프1\wsj_partial.txt", "r") as f1:
    text = f1.read()

word_pat = re.compile(r"(\w+|\.|,)/")

words = word_pat.findall(text)

print("\n#########################")
print("#### 단어만 추출하기 ####")
print("#########################\n")
print(words)

# 단어들 합치기
sent = ' '.join(words)

# 문장 분리하고 전처리
if '.' in sent:
    sent = re.sub(r'( \.)', '.\n', sent)
    sent = re.sub(r'\n ', '\n',sent)
    sent = re.sub(r'( ,)', ',', sent)

sents = sent.split('\n')
del sents[-1]

print("\n#############################")
print("#### 문장단위로 추출하기 ####")
print("#############################\n")

n = 1
for sent in sents:
    print(str(n) + ": " + sent)
    n += 1
