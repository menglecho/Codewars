def order(sentence):
    sen_split = sentence.split()
    return ' '.join(sorted(sen_split,key=getNumber))
    
def getNumber(stringInput):
    for w in stringInput:
        for l in w:
            if l.isdigit():
                return l

# Clever solution, using lambda and filter function

def order_clever(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int("".join(filter(str.isdigit, x)))))