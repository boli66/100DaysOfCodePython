from libraries import l
scores= input("Enter the students scores seperated py spaces: ").split(" ")
scores = l.intl.list(scores)
names = input("Enter the students names in the order you entered their points: ").split(" ")
highest_score = scores[0]

for score in scores:
    if highest_score < score:
        highest_score = score

highest_score = scores.index(highest_score)

print(f"{names[highest_score]} got {scores[highest_score]} points. He won!")