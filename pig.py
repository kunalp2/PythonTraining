inputSentence = input("Please enter an input sentence to translate:").strip().lower()

listOfWords = inputSentence.split()
vowels = "aeiou"
newWords = []

for word in listOfWords:
    if word[0] in vowels:
        newWord = word + "yay"
        newWords.append(newWord)
    else:
        pos = 0
        for ltr in word:
            if ltr not in vowels:
                pos = pos + 1
            else:
                break
        cons = word[:pos]
        theRest = word[pos:]
        newWord = theRest + cons + "ay"
        newWords.append(newWord)

output = " ".join(newWords)
print(output)