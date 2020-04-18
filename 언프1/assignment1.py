alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

# 소문자로 바꾸기

lower_alice = alice.lower()
print("1", lower_alice)

# 마침표 삭제하기

no_punct_alice = alice.replace('.', '')
print('2', no_punct_alice)

# “the”를 “THE”로 바꾸기 (cf. THEn)

the_changed_alice = alice.replace('the', 'THE')
print('3', the_changed_alice)

# 띄어쓰기로 분할하기

tokenized_alice = alice.split()

print('4', tokenized_alice)