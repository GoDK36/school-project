def inflection(word):
    infl_dic = {"sheep":1, 'book':1, 'box':2, 'city':3, 'wife': 4, 'leaf':5}
    if word in infl_dic.keys():
        if infl_dic[word] == 1:
            res = word + 's'
            print(res)
        elif infl_dic[word] == 2:
            res = word + 'es'
            print(res)
        elif infl_dic[word] == 3:
            res = word[:-1] + 'ies'
            print(res)
        elif infl_dic[word] == 4:
            res = word[:-2] + 'ves'
            print(res)
        elif infl_dic[word] == 5:
            res = word[:-1] + 'ves'
            print(res)

inflection(input("Which word do you want to change? "))

def plural(word):
    if word[-1] == 'y':
        res = word[:-1] + 'ies'
        print(res)
    elif word[-2:] == 'fe':
        res = word[:-2] + 'ves'
        print(res)
    elif word[-1] == 'f':
        res = word[:-1] + 'ves'
        print(res)
    elif word[-1] == 'x' or word[-1] == 's' or word[-1] == 'z':
        res = word + 'es'
        print(res)
    else:
        res = word + 's'
        print(res)

# plural(input("Which word do you want to change? "))                ## irregular는 따로 사전이 필요할듯합니다....