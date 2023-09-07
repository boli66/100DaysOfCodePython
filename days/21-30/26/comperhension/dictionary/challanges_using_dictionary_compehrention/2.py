from lib import *
days = [s.title() for s in
        ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        ]
temps = [12,14,15,14,21,22,24]

weather_c = {days[i]:temps[i] for i in range(len(days))}

def c_to_f(c):
        return c*9/5+32

weather_f = {day:c_to_f(temp) for day,temp in weather_c.items()}
print(Format(weather_f))