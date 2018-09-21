import os
import random
import itertools


def parse_row(row):
    row_part = row.split(';')
    return [row_part[0], row_part[1].split(' ')[0], row_part[1].split(' ')[1], row_part[2].split(' ')[0]]


def parse_files_in_cur_folder():
    current_folder = os.getcwd()
    payments = []
    for i in os.listdir(current_folder):
        if os.path.isfile(i) and i.endswith('.txt'):
            # print('File {0}:'.format(i))
            with open(i) as file:
                rows_list = [row for row in file.readlines() if row.find('out') >= 0]
            for row in rows_list:
                payments.append(parse_row(row))
            # print(payments)
    return payments


class Person:
    def __init__(self, name):
        self.name = name
        self.birthDate = random.randint(1970, 1990)

    def getBirthDate(self):
        return self.birthDate

    def getName(self):
        return self.name


parsed_list = parse_files_in_cur_folder()
names = set(n[0] for n in parsed_list)
days = set(n[3] for n in parsed_list)
currencies = set(n[2] for n in parsed_list)


# 2) get list of all Persns and sort them by birthDate
persons_list = []
for name in names:
    persons_list.append(Person(name))
persons_list.sort(key=lambda x: x.getBirthDate())
for person in persons_list:
    print('{0} was born in {1}'.format(person.getName(), person.getBirthDate()))


# 3) create Payer class, Payment class
class Payment:
    def __init__(self, amount, currency, date):
        self.amount = amount
        self.currency = currency
        self.date = date

    def getAmount(self):
        return self.amount

    def getCurrency(self):
        return self.currency

    def getDate(self):
        return self.date


class Payer(Person, Payment):
    """docstring for Payer"Person, Payment"""

    def __init__(self, name, amount, currency, date):
        Person.__init__(self, name)
        Payment.__init__(self, amount, currency, date)


# payers_list = []
# for pr in parsed_list:
#     payers_list.append(Payer(pr[0], pr[1], pr[2], pr[3]))
# for payer in payers_list:
#     print('Name: {0}; Birth Date: {1}; Amount: {2}; Currency: {3}; Date of Payment: {4}'.
#           format(payer.getName(), payer.getBirthDate(), payer.getAmount(), payer.getCurrency(), payer.getDate()))


# 1) Count number of payments and the total number of payments in each currency per day
payments_list = []
count = 0
total_amount = 0
amount_per_day = {day: 0 for day in days}
amount_per_currency = {day: 0 for day in currencies}

for element in parsed_list:
    payments_list.append(Payment(element[1].replace(',', '.'), element[2], element[3]))
for payment in payments_list:
    amount_per_day[payment.getDate()] += float(payment.getAmount())
    amount_per_currency[payment.getCurrency()] += float(payment.getAmount())
    count += 1
    total_amount += float(payment.getAmount())
print('Amount per day: ')
print(amount_per_day)
print('Amount per currency: ')
print(amount_per_currency)
print('Count of payments: ')
print(count)
print('Total amount: ')
print(total_amount)
