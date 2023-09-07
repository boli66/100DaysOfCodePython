student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

import pandas

data = pandas.DataFrame(student_dict)

s = [row["score"] for index,row in data.iterrows()]

from lib import *
print(FormatList(s))
