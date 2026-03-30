##

import csv
with open('./day02/부산시 해운대구 도서정보.csv','r',encoding='utf-8') as f:
    reader = csv/reader(f)

    for row in reader:
        print(row)