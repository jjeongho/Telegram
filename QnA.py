import csv

f = open('C:/Users/JJeong/PycharmProjects/Telegram/Kava.csv', 'r')
rdr = csv.reader(f)

for line in rdr:
    print(line)

f.close()