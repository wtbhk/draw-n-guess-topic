import json

f = open("data.txt", "r")
d = f.read()
d = d.split()

print(json.dumps([[row, 1] for row in d], ensure_ascii=False))
