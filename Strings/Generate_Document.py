'''
The prompt: given two strings, document and characters, can document be created by the characters available in characters.
'''



def generate_doc(characters,document):
    for i in range(len(document)):
        doc_freq = cal_freq(document[i],document)
        ch_freq = cal_freq(document[i],characters)
        if doc_freq > ch_freq:
            return False

    return True


def cal_freq(character, document):
    freq = 0
    for i in range(len(document)):
        if (document[i] == character):
            freq+=1
    return(freq)


if __name__ == '__main__':
    bool = False
    ch = "helloworldO"
    doc = "hello wOrld"
    bool = generate_doc(ch,doc)
    print(bool)