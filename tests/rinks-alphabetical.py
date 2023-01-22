import json
import re

def customSort(word):
    # Crazy Norwegian Sort
    alphabet = list(
        " AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÆæÄäØøÖöÅå-’'`!?*&+/.,:;"
    )
    d = re.findall("(\d+)", word)
    # Custom handling of ints
    if d:
        w = word
        w2 = []
        for a in d:
            p = w.split(a, 1)
            w = p[1]
            w2.append(p[0])
            w2.append(int(a))
        w2.append(w)
        res = []
        for e in w2:
            if isinstance(e, int):
                res.append(len(alphabet) + e)
            else:
                for l in e:
                    res.append(alphabet.index(l))
        return res
    return [alphabet.index(c) for c in word]

with open("rinks.json") as f:
    data = json.load(f)

names = []
for rink in data:
    name = rink["id"]
    if not name or len(name.strip()) == 0:
        name = rink["name"]
    names.append(name.strip())

sorted_names = sorted(names, key=lambda word: customSort(word))

errors = False
for index in range(len(names)):
    if sorted_names[index] != names[index]:
        print(index, names[index], "is in the wrong location!")
        errors = True

if errors:
    exit(1)
