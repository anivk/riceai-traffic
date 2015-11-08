__author__ = 'Tian'

import csv

#f = open("test_csv.csv")

fieldnames = ['h1', 'h2', 'h3']

c = open("test_csv.csv", 'a', newline='')
try:
    writer = csv.writer(c)
    writer.writerow( fieldnames )
    writer.writerow([5,3,"hello"])
    writer.writerow([2,'lol lol', 'hello,.js'])
finally:
    c.close()

