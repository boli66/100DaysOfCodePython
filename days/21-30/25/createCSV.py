import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
#data.to_csv("example.csv")

data = pandas.read_csv("dd.csv")
print(data)