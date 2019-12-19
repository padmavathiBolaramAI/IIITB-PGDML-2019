import csv
import json
cities =[]
with open('cities.csv', "r") as csvfile:
    reader = csv.reader(csvfile)
    cities = [row[0] for row in reader]



data ={}
fd =[]
for i in cities:
    data["text"] = i
    data["intent"] = "restaurant_search"
    data["entities"] = [{"start": 0, "end": len(i) ,"value": i, "entity": "location"}]
    fd.append(data.copy())


str = ''
for i in fd:
    str += json.dumps(i, ensure_ascii = False, indent=2) + ',' + "\n"


text_file = open("Output.txt", "w")
text_file.write(str)
text_file.close()