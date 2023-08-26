travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

"""#TODO: Write the function that will allow new countries"""
#to be added to the travel_log. 👇
def add_new_country(name, times_visited, cities_visited):
    newCountry = {"country": name, "visit s": times_visited, "cities": cities_visited}
    travel_log.append(newCountry)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)