from re import split

sentence = ""
ans = ""
tempt = True
def string_play(sentence):
    global tempt
    if sentence == "":
        sentence = (input('enter full sentence: '))
        result = (sentence.split(" "))
        length = len(result)
        print('Sentence split into', length, "words:", result)
        tempt = False
    else:
       print('enter a sentence')
while tempt:
    string_play(ans)