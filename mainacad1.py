import datetime
import string
import random


def read_logs(fileName):
    # read file
    with open(fileName, 'r') as file:
        # read lines with ERROR in a list
        err_rows = [row for row in file.read().split(
            '\n') if row.find('[ERROR]') > 0]

    # populate output
    new_rows = []
    for row in err_rows:
        # output line
        mes_info = row.split()
        message = row.split(' - ')[1]
        output_line = 'ip address: ' + \
            mes_info[0] + ', error_time: ' + \
            mes_info[2] + ', message: ' + message
        new_rows.append(output_line + '\n')

    print(new_rows)

    # forming new file
    with open(fileName + '_errors', 'w') as err_file:
        err_file.writelines(new_rows)


# read_logs('C:/UBS/Dev/temp/temp_temp/logs.txt')

def get_sentence(phrase):
    # remove punctuation
    l = [el for el in list(phrase) if el not in string.punctuation]
    l = ''.join(l).lower()
    # replace new row on space and split by spaces
    l = l.replace('\n', ' ').split(' ')
    # remove empty elements
    l = [el for el in l if el != '']
    # remove dublicates by casting to set
    l = list(set(l))
    print (l)
    new_phrase = ''
    for x in range(random.randint(5, 10)):
        r = random.randint(0, len(l) - 1)
        print(r)
        if x == 1:
            new_phrase = new_phrase.title()
        new_phrase = new_phrase + ' ' + l[r]

    new_phrase = new_phrase + '.'
    print(new_phrase)


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

get_sentence(input_phrase)
