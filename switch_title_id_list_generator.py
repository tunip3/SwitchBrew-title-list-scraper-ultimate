import xml.etree.ElementTree as ET
import urllib.request
import os
import csv
import mmap
import wikitablescrape
urllib.request.urlretrieve('http://nswdb.com/xml.php', 'db.xml')
tree = ET.parse('db.xml')
root = tree.getroot()

count = 0
loop=True
tidlist=[]

while loop == True:
    filename = input("do you want to set a custom name for the title id list \nor leave it as the default (eNXhop.txt for use with eNXhop) \ncustom or default:")
    if filename == "custom":
        filename = input("please enter a name for the output including a file extension: ")
        loop=False
    if filename == "default":
        filename = "eNXhop.txt"
        loop=False
    else:
        print("please enter custom or default\n")
try:
    os.remove(filename)
except:
    pass

for titleid in root.iter('titleid'):
    tid= titleid.text
    if tid != None:
        tidlist.append(tid+"\n")
        print(tid)

try:
    os.remove('TitleID/TitleID.csv')
except:
    pass

wikitablescrape.scrape(
    url="http://switchbrew.org/index.php?title=Title_list/Games",
    output_name="TitleID"
)
		
f = open('TitleID/TitleID.csv', encoding="utf8")
csv_f = csv.reader(f)

for row in csv_f:
  if (not(row[6]) == "Type") and (not(row[6]) == "Update"):
    tid = row[0]
    tidlist.append(tid+"\n")
    print(tid)

f.close()
file = open(filename,"w")
file.writelines(set(tidlist))
file.close()

os.remove("db.xml")
