import pandas
from lib import *

# Get the word from the user
IN = input("Enter a word: ")

# Get the data
datas = pandas.read_csv("./nato_phonetic_alphabet.csv")

# Format the data
data = {row["letter"]:row["code"] for i,row in datas.iterrows()}


# Covert a letter to the NATO Alphabet
def covert(letter):
    l = letter.upper()
    if(l in data):
        return data[l]
    return letter

# Print the word in NATO
nato = [covert(l) for l in IN]


print(nato)