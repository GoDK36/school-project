alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

# 1. 띄어쓰기 단위로 분할하기

sep_alice = alice.split()

print("####################################")
print("######## 1. 띄어쓰기한 alice ########")
print("####################################")
print('\n', sep_alice, "\n")

# 2. "the"가 몇 번 등장하는지 구하기

cnt_the = sep_alice.count("the")

print("####################################")
print("########### 2. the 빈도 ############")
print("####################################")
print('\n', cnt_the, '\n')

# 2-1 " 빈도 구하기 (과제 섹션에는 " 빈도 구하기로 되어있어서 혹시나하는 마음에 같이 해봅니다...!)

cnt_double_qut = alice.count('"')

print("####################################")
print("########### 2. \" 빈도 #############")
print("####################################")
print('\n', cnt_double_qut, '\n')

# 3. unique word list 만들기

unique_word_list = list(set(sep_alice))


print("####################################")
print("#### 3. unique word list 만들기 ####")
print("####################################")
print('\n', unique_word_list, '\n')

# # 3-1 진짜 단어만 남기기(부호 제거)

# real_uni_wrd_lst = []
# for x in unique_word_list:
#     if "." in x:
#         p_del = x.replace('.', '')
#         real_uni_wrd_lst.append(p_del)
#     elif '"' in x:
#         d_q_del = x.replace('"','')
#         real_uni_wrd_lst.append(d_q_del)
#     elif ',' in x:                    # ME," 를 못 잡음 / while을 써서 원하는 punct가 제거될때까지 돌리는 방법이 더 나을 수도
#         com_del = x.replace(',','')
#         print(com_del)
#         real_uni_wrd_lst.append(com_del)
#     else:
#         real_uni_wrd_lst.append(x)
# real_uni_wrd_lst.sort()

# print("############################################")
# print("#### 3-1. 진짜 단어만 남기기(부호 제거) ####")
# print("###################################3########")
# print('\n', real_uni_wrd_lst, '\n')

# 4. 3의 목록을 오름차순으로 정렬

sorted_alice = sorted(unique_word_list)

print("########################################")
print("#### 4. 3의 목록을 오름차순으로 정렬 ####")
print("########################################")
print('\n', sorted_alice, '\n')
