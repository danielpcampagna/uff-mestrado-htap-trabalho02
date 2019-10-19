#!/usr/bin/python3
#coding: utf-8

import csv
import time
from datetime import datetime
# import os

def generate_milisec_from_date(inname, date_column, outname, fieldnames):
    # print(os.path.exists(inname))
    # print(os.path.exists(outname))

    with open(inname) as infile:
        reader = csv.DictReader(infile)
        # reader = csv.reader(infile)
        
        with open(outname, 'w+', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            print('inicio')
            for row in reader:
                print(date_column not in row)
                if date_column not in row:
                    break
                
                date = row[date_column] # '10/11/2017 12:30:00 PM'
                milisec = strdate_to_milisec(date)

                row[f'{date_column}_milisec'] = milisec
                writer.writerow(row)
            print('fim')

def strdate_to_milisec(val):
    result = datetime.strptime(val, '%d/%m/%Y %H:%M:%S %p')
    return time.mktime(result.timetuple())*1000

if (__name__ == '__main__'):
    inname = './denver-crime-data/crime.csv'
    outname = './crime-generate_milisec_from_date.csv'
    fieldnames = [
        "INCIDENT_ID", "OFFENSE_ID", "OFFENSE_CODE",
        "OFFENSE_CODE_EXTENSION", "OFFENSE_TYPE_ID",
        "OFFENSE_CATEGORY_ID", "FIRST_OCCURRENCE_DATE",
        "LAST_OCCURRENCE_DATE", "REPORTED_DATE", "INCIDENT_ADDRESS",
        "GEO_X", "GEO_Y", "GEO_LON", "GEO_LAT", "DISTRICT_ID",
        "PRECINCT_ID", "NEIGHBORHOOD_ID", "IS_CRIME", "IS_TRAFFIC"
    ]

    generate_milisec_from_date(inname, 'REPORTED_DATE', outname, fieldnames)



