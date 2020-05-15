alice = 'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes.'

def find_word_alice(word=input("input word you want to find: ")):
    # alice 데이터 전처리
    low_alice = alice.lower()
    del_punc_alice = low_alice.replace(",", '')
    del_punc_alice = del_punc_alice.replace('\'', '')
    del_punc_alice = del_punc_alice.replace('.', '')
    del_punc_alice = del_punc_alice.replace('"', '')

    # alice 데이터 어절 단위로 분리
    sep_alice = del_punc_alice.split()

    result = sep_alice.count(word)

    if result == 0 :
        print("The word you entered is not found")
    else:
        print(result)
        


find_word_alice()