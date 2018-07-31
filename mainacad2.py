import string


def read_this(in_phrase):
    l0 = in_phrase.replace('\n', ' ').split(' ')
    l1 = []
    for i in l0:
        t = [el for el in list(i) if el not in string.punctuation]
        t = ''.join(t).lower() + '\n'
        if t != '\n':
            l1.append(t)  # fill non sorted with dublicates
    l0 = list(set(l1))
    l1 = sorted(l0, reverse=True)
    l0.sort()
    # Task #1 - create files with sorted in asc/desc way
    with open('file_asc.txt', 'w') as f0:
        f0.writelines(l0)
    with open('file_desc.txt', 'w') as f1:
        f1.writelines(l1)
    # Task #2 - find the biggest and smallest world
    l2 = sorted(l0, key=lambda x: len(x))
    print('Longest word is ' + l2[0])
    print('Shortest word is ' + l2[-1])
    # Task #3 - form dict like [a: [word_with_a,word_with_a2...], b:[...] ...]
    counter = {key: [] for key in string.ascii_lowercase}
    print(counter)
    for i in l0:
        for letter in counter:
            if letter in i:
                counter[letter].append(i)
    print (counter)


# Task #4 - cipher of Caesar with shift = 4
def caesar_cipher(in_phrase):
    alphabet = list(string.ascii_lowercase)
    alphabet.sort()
    caesar = {}
    for i in alphabet:
        caesar[i] = alphabet[(alphabet.index(i) + 4) % 26]
    # print (caesar)
    output_phrase = []
    for i in list(in_phrase.lower()):
        if i in caesar.keys():
            output_phrase.append(caesar[i])
        else:
            output_phrase.append(i)
    print(''.join(output_phrase))

input_phrase = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''


read_this(input_phrase)


caesar_cipher(input_phrase)

