import pandas

data = pandas.read_csv("weather_data.csv")

#temps = round(data["temp"].max())
#print(f"The highest temperature was {temps} celcius last week.")

#print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
temp = monday["temp"]
temp = temp*1.8+32
print(monday.temp)
print(temp)
