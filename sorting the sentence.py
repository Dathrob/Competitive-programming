#40 min
def sortSentence(str):
    sliced = str.split()
    new_hash = dict()
    count = -1
    new_sentence = []
    sentence = ""
    for i in sliced:
        count+=1 
        for j in i:
            if j.isnumeric():
                j = int(j)
                word = sliced[count]
                new_hash[j] =  word[:-1]
    for i in range(1,len(sliced)+1):
        str = "".join([new_hash[i]])
        sentence = sentence + str + " " 
    print(sentence)
sortSentence("is2 sentence4 This1 a3")
    