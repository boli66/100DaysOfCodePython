import json
from ui import UI

def appendJSON(data,path):
    with open(path) as f:
        d = json.load(f)
        d.append(data)
    with open(path, "w") as f:
        json.dump(d, f, indent=4)

def add():
    response = ui.getQuestion()
    if(response == None): return
    ui.clear()
    appendJSON(response, "db.json")
    ui.update()

ui = UI()

ui.submit["command"] = add

ui.mainloop()