import csv
import string

from excel import *

def n2a(n,b=string.ascii_uppercase):
   d, m = divmod(n,len(b))
   return n2a(d-1,b)+b[m] if d else b[m]

def save_csv(file_path, csv_data):
    with open(file_path,'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerows(csv_data)

def load_csv(file_path):
    csv_data = list(csv.reader(open(file_path)))
    for x in range(len(csv_data)):
        for y in range(len(csv_data[x])):
            cell_pos = f'{n2a(y)}{x+1}'
            globals()[cell_pos] = csv_data[x][y]

if __name__ == '__main__':
    print(ARABIC('LVII'))
    print(ARABIC('LIV'))
    # load_csv('example.csv')
    print(ACOS(0.5))
    print(ACOSH(1.5))
    print(FISHER(0.75))
    print(FISHERINV(FISHER(0.75)))
    # print(B2)