import csv
import sys
from datetime import datetime, timedelta




school_holidays = []
work_holidays = []

#read school holidays
with open(sys.argv[1], 'r', encoding='cp1252') as csv_file:  
    
    csv_reader = list(csv.DictReader(csv_file, delimiter=";"))
   

    if csv_reader:  
        
        first_row = csv_reader[0]
        start_date = datetime.strptime(first_row["Date"], "%d.%m.%Y")

        last_row = csv_reader[-1]
        end_date = datetime.strptime(last_row["End"], "%d.%m.%Y")
    

    for line in csv_reader:
        start = datetime.strptime(line["Date"], "%d.%m.%Y")
        stop = datetime.strptime(line["End"], "%d.%m.%Y")
        school_holidays.append((start, stop))
    

#read work holidays
with open(sys.argv[2], 'r', encoding='cp1252') as csv_file:  
    
    csv_reader = list(csv.DictReader(csv_file, delimiter=";"))
    

    for line in csv_reader:
        start = datetime.strptime(line["Date"], "%d.%m.%Y")
        stop = datetime.strptime(line["Date"], "%d.%m.%Y")
        work_holidays.append((start, stop))
    


with open(sys.argv[3], 'w', newline='', encoding='utf-8') as new_file:

    fieldNames = ["date", "is-school", "is-holiday", "weekday"]
    csv_writer = csv.DictWriter(new_file, delimiter=',', fieldnames=fieldNames)
    csv_writer.writeheader()

    curr_date = start_date
    while curr_date <= end_date:
        
        in_school_holiday = any(start <= curr_date <= stop for start, stop in school_holidays)
        in_work_holiday = any(start <= curr_date <= stop for start, stop in work_holidays)

        in_weekend = curr_date.weekday() >= 5
        
        row = {
            "date": curr_date.strftime("%Y-%m-%d"),
            "is-school": 0 if (in_school_holiday or in_weekend)  else 1,
            "is-holiday": 1 if (in_work_holiday or in_weekend) else 0,
            "weekday" : curr_date.strftime("%a")
        }
        csv_writer.writerow(row)
        curr_date += timedelta(days=1)
