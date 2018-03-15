import json, re
text = ""
with open("genres.js",'r') as file:
    text = file.read()
matches = re.findall(r'(.*) \xe2(.*)\n',text)
jsonMatches = []
for match in matches:
   jsonMatches.append(match[0])
# print jsonMatches
with open("dump.json",'w') as file:
    file.write(json.dumps(jsonMatches))