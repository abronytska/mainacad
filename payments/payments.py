import os


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



parsed_list = parse_files_in_cur_folder()
names = set(n[0] for n in parsed_list)
result_list = [[d, 0, 0, 0] for d in names]

for result_row in result_list:
    for nm, payment, currency, date in parsed_list:
        if result_row[0] == nm and currency == 'EUR':
            result_row[1] += float(payment.replace(',', '.'))
        if result_row[0] == nm and currency == 'USD':
            result_row[2] += float(payment.replace(',', '.'))
        if result_row[0] == nm:
            result_row[3] += 1
result_list = sorted(result_list, key=lambda x: x[3])
for i in result_list:
    print(i)
