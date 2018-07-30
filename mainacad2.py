import string


def read_this(in_phrase):
    l = in_phrase.replace('\n', ' ').split(' ')
    l1 = []
    for i in l:
        i = ''.join(
            [el for el in list(i) if el not in string.punctuation]).lower() + '\n'
        if i != '\n':
            l.append(i)  # fill non sorted with dublicates
    l1 = list(set(l))
    l2 = sorted(l1, reverse=True)
    l1.sort()
    # Task #1 - create files with sorted in asc/desc way
    with open('file_asc.txt', 'w') as f1:
        f1.writelines(l1)
    with open('file_desc.txt', 'w') as f:
        f.writelines(l2)
    # Task #2 - find the biggest and smallest world
    l3 = sorted(l1, key=lambda x: len(x))
    print('Longest word is ' + l3[0])
    print('Shortest word is ' + l3[-1])
    # Task #3 - form dict like [a: [word_with_a,word_with_a2...], b:[...] ...]


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
