vowel = ['a', 'e', 'i', 'o', 'u']

sent = input('Please enter your sentence to be translated into Pig_latin language: ')
sen = sent.split()

piglatin = []
def vowel_change(word):
    if word[0] in vowel:
        new = word + 'way'
        piglatin.append(new)
    else:
        pass

def other_change(word):
    if word[0] not in vowel:
        new = word[1:] + word[0] + 'ay'
        piglatin.append(new)
    else:
        pass

def translator(sentence):
    for w in sentence:
        vowel_change(w)
        other_change(w)
    new_sentence = ' '.join(piglatin)
    print(new_sentence)

translator(sen)