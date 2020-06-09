
def print_string(text):
    f1 = open(r"E:\Develop\python\school-project\언프1\\" + text, "r")
    strings = f1.read()
    
    return strings
    f1.close()

print("\n#############################")
print("#### source.txt 불러오기 ####")
print("#############################\n")

text = print_string("source.txt")
print(text)

def word_list(text):
    lower_text = text.lower()

    del_punc_text = lower_text.replace(",", '')
    del_punc_text = del_punc_text.replace('\'', '')
    del_punc_text = del_punc_text.replace('!', '')
    del_punc_text = del_punc_text.replace('.', '')
    del_punc_text = del_punc_text.replace('[', '')
    del_punc_text = del_punc_text.replace(']', '')
    del_punc_text = del_punc_text.replace('?', '')
    del_punc_text = del_punc_text.replace(':', '')
    del_punc_text = del_punc_text.replace(';', '')
    del_punc_text = del_punc_text.replace('"', '')
    del_punc_text = del_punc_text.replace('(', '')
    del_punc_text = del_punc_text.replace(')', '')
    wrd_text = del_punc_text.split()

    unique_word_list = list(set(wrd_text))
    unique_word_list.sort()

    return wrd_text, unique_word_list

print("\n#########################")
print("#### 단어리스트 출력 ####")
print("##########################\n")

word_text, unique_word_list = word_list(text)
print(unique_word_list)

def word_count(text):
    word_text, unique_word_list = word_list(text)

    word_dict = {}
    for word in unique_word_list:
        word_dict[word] = word_text.count(word)

    for word, freq in word_dict.items():
        print(word + ': ' + str(freq))

print("\n###########################")
print("#### 단어: 빈도로 출력 ####")
print("###########################\n")

word_count(text)

