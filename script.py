#!/usr/bin/env python3

from bs4 import BeautifulSoup
import glob
import os
import csv

path = "/Users/..."

for filename in glob.glob(os.path.join(path, "*.xml")):
        with open(filename) as open_file:
            content = open_file.read()
            soup = BeautifulSoup(content, "xml")
            titles = soup.find("book-title")
            subjects = soup.find("subject")
            years = soup.find("year")
            isbn = soup.find("isbn")
            href = soup.find("self-uri")
            print(titles, subjects, years, isbn, href['xlink:href'])
        with open(path+'document.csv','a') as fd:
        	writer = csv.writer(fd, delimiter=',')
        	csvStructure = [titles.text, subjects.text, years.text, isbn.text, href['xlink:href']]
        	writer.writerow(csvStructure)
        	print("Done!")
