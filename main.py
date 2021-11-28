def sort_sentence(sentence):
    sentence = sentence.lower()
    sentence = sentence.split(' ')
    sentence_len = []
    for s in sentence:
        sentence_len.append((len(s), s))
    sentence_len = sort(sentence_len)
    sentence = []
    for s in sentence_len:
        sentence.append(s[1])
    sentence = " ".join(sentence)
    sentence = sentence.capitalize()

    return sentence


def sort(array):


    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0][0]
        for x in array:
            if x[0] < pivot:
                less.append(x)
            elif x[0] == pivot:
                equal.append(x)
            elif x[0] > pivot:
                greater.append(x)

        return sort(less)+equal+sort(greater)

    else:
        return array

if __name__ == "__main__":
    sentence = "Keep calm and carry on"
    print(sort_sentence(sentence))
