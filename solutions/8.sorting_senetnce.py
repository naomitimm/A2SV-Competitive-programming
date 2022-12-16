def sortSentence(sentence):
    words = sentence.split()
    sentenceList = []

    for word in words:
        index = int(word[-1])
        sentenceList.insert(index - 1, word[:-1])
 
    result = ' '.join(sentenceList)
    print(result)

sortSentence("Myself2 Me1 I4 and3")