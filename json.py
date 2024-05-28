'''  ========================= ** Main 2 ** ====================================== '''

print(__doc__)

import json 

# Doc file
# with open('data.json', mode='r') as file:
#   list = json.load(file)
#   print(json.dumps(list, indent=4))

student = [
  {
  "name": "Van Cong",
  "age": "28",
  "address": "Tb",
  "phone": "034757968",
  },
  {
  "name": "Congkaka",
  "age": "29",
  "address": "Tb",
  "phone": "0972006977",
  },

]

student2 = [
  {
  "name": "Van Cong 1",
  "age": "28",
  "address": "Tb",
  "phone": "034757968",
  },
  {
  "name": "Congkaka 1",
  "age": "29",
  "address": "Tb",
  "phone": "0972006977",
  },

]

# add data to a json file
# with open('data1.json', mode='w') as file:
#   json.dump(student, file, indent= 4)


with open('data.json', mode='r') as file:
  jsonFile = json.load(file)
  

  jsonFile.extend(student2)

with open('data.json', mode='w') as file:
  json.dump(jsonFile, file, indent=1)
