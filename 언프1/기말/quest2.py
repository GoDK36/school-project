import re

print("#####################################")
print("####### 2-1 단어-품사 딕셔너리 #######")
print("#####################################")
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
print("###########################################")
print("######## 2-2 활용형 원형으로 바꾸기 ########")
print("###########################################")
print()

