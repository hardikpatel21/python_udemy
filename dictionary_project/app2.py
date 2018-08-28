import json

data = json.load(open("data.json"))
def translet(w):
    w = w.lower()
    result = ""
    if w in data:
        for meaning in data[w]:
            result += "\n"+meaning + "\n"
        return result

    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

print(translet(word))
