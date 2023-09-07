import data

def covertLetter(letter:str):
    letter = letter.upper()
    if(letter in data.covertion):
        return data.covertion[letter]

word = input("Enter a word: ")

out = [covertLetter(n) for n in word]

print(out)
