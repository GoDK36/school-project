################################################################
################ Just Change this sections #####################
################################################################
# (1) Type Your Sentence

sents = ["The company hired a man with sincerity.",
        "Which option do you want to select?",
        "The shop manager wrote an email to the customer.",
        "While you were taking a nap, I was working overtime.",
        "The professor permitted the students to take a nap during the class."]

# (2) Make your CFG file for parsing your sentence.

# ex. grammar.cfg (see the direction in the powerpoint)

################################################################

import nltk
grammar = nltk.data.load(r"file:E:\Develop\python\school-project\컴언\NLTK\NLTK\cfg 파일\new_grammar.cfg")
parser = nltk.ChartParser(grammar)

n = 1
for sent in sents:
    tokens = nltk.tokenize.word_tokenize(sent)
    trees = parser.parse(tokens)

    with open(r"E:\Develop\python\school-project\컴언\result" + str(n) + ".txt", "w") as f1:
        for tree in trees:
            print(tree)
            f1.write(str(tree)+"\n\n")
            tree.draw()
    f1.close()
    
    n += 1

"""
단어를 정확히 입력??(구두점까지?)
너무 많이 가지수가 나옴


참고 사이트
http://erg.delph-in.net/logon
https://www.link.cs.cmu.edu/cgi-bin/link/construct-page-4.cgi#submit

"""