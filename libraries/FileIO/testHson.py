import hson
#
# json = hson.json("dc.json", {})
#
# obj = {
#     "Hello": "Greetings traveler."
# }
# json.obj = obj
#
# json.save()
js = hson.hson("dc.txt",{}).get()
print(js["Hello"])
print(type(js))