
answers = ["skjuts", "shoppingcenter", "schysst", "ljuga", "djungel", "chocklad", "t-shirt", "jacka"
    ,"gillar",
           "yoghurt",
           "information",
           "gjort",
           "hjortar",
           "stjärnorna",
           "generad"
]
def inWhiteSpaces(word):
    s = ""
    for i in range(0,len(word)):
        s+="_"
    return s
questions = [
    f'Kan jag få {inWhiteSpaces("skjuts")} hem?',
    f'Nacka forum är ett {inWhiteSpaces("shoppingcenter")}.',
    f'Det är bra att vara {inWhiteSpaces("schysst")} mot andra.',
    f'Det är dåligt at {inWhiteSpaces("ljuga")}.',
    f'Det finns mycket finna och farliga djur i en {inWhiteSpaces("djungel")}',
    f'{inWhiteSpaces("chocklad")} är en brun och good sak.',
    f'Man har ofta en {inWhiteSpaces("t-shirt")} när det är varmt.',
    f'Det är bra at ha en {inWhiteSpaces("jacka")} när det blir kalt och regnigt.',
    f'Jag {inWhiteSpaces("gillar")} att åka gokart.',
    f'{inWhiteSpaces("yoghurt")} är en bra och enkel fruckost.',
    f'Google har mycket {inWhiteSpaces("information")} om dig.',
    f'Jag har {inWhiteSpaces("gjort")} en paj år dig och dina vänner.',
    f'Det finns mest {inWhiteSpaces("hjortar")} i Nordamerika.',
    f'{inWhiteSpaces("stjärnorna")} är finna på natten',
    f'Jag kände mig {inWhiteSpaces("generad")} när jag behövde presentera min presentation för klassen.'
]
score = 0
for i in range(0,len(questions)):
    print(questions[i])
    In = input("Write the missing word: ").lower()
    if(In.lower() == answers[i]):
        score+=1
    else:
        print(f"Wrong the right answer was {answers[i]}")
    print("")
print(f"Your score is {score}/{len(questions)}")

