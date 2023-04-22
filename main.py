import json

f = open("data.txt", "r")
d = f.read()
d = d.split()

output = json.dumps([[row, 1] for row in d], ensure_ascii=False, separators=(',', ':'))
print(output)

fw = open("output.json", "w")
fw.write(output)

f.close()
fw.close()
