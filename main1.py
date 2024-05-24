'''  ========================= ** Main 1 ** ====================================== '''

print(__doc__)

import csv
import json

# with open('data.csv', mode= 'r', encoding ='utf8') as file:
#   # for line in file:
#   #   print(line.strip())
#   csv_file = csv.DictReader(file)
#   list = list(csv_file)
#   # print(json.dumps(list, indent=1))

#   for item in list:
#     print(item)
header = ["name", "age", "address"]
values = [
  ["congkaka", "18", "TB"],
  ["congkaka1", "19", "AT"],
]
with open('data1.csv', mode='w', newline='') as file:
  csv_write = csv.writer(file)
  csv_write.writerow(header)
  csv_write.writerow(values)


