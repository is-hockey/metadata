import json
import re

def customSort(word):
    # Define the alphabet used for sorting
    alphabet = list(" AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÆæÄäØøÖöÅå-’'`!?*&+/.,:;")
    
    # Find all occurrences of digits in the word
    digits = re.findall("(\d+)", word)
    
    # Custom handling of digits
    if digits:
        remaining_word = word
        sorted_word = []
        
        # Split the word at each digit and append the parts to the sorted word list
        for digit in digits:
            parts = remaining_word.split(digit, 1)
            remaining_word = parts[1]
            sorted_word.append(parts[0])
            sorted_word.append(int(digit))
        
        # Append the remaining part of the word
        sorted_word.append(remaining_word)
        
        # Convert characters and digits to numerical values based on the alphabet
        result = []
        for element in sorted_word:
            if isinstance(element, int):
                result.append(len(alphabet) + element)
            else:
                for char in element:
                    result.append(alphabet.index(char))
        
        return result
    
    # If no digits are found, sort the word based on the alphabet
    return [alphabet.index(char) for char in word]

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
        print("*" * 10, index, names[index], "is in the wrong location!")
        errors = True
    else:
        print(index, names[index], "is in the correct location!")

if errors:
    exit(1)
