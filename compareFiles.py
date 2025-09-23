import csv
import sys

exit = False

with open(sys.argv[1], 'r', encoding='utf-8') as csv_file_1:  
    csv_reader_1 = list(csv.DictReader(csv_file_1, delimiter=","))

with open(sys.argv[2], 'r', encoding='utf-8') as csv_file_2:  
    csv_reader_2 = list(csv.DictReader(csv_file_2, delimiter=","))

if  len(csv_reader_1) != len(csv_reader_2):
    print("length not matching")
    exit = True

for line1, line2 in zip(csv_reader_1, csv_reader_2):

    if line1 != line2:
        print("lines not matching: " + str(line1) + " != " + str(line2))
        exit = True

if(exit):
    sys.exit(1)


print("CSV files are identical")