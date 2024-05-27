# import to_gson
import json


with open('C:/Users/alien/Documents/Loyiha/Alien/sources/dictup/book/essential/strings/story.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


for i in data:
    print(i)
# print(dat.get(0)["story.json"])
