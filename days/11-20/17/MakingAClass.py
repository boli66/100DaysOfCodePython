class User:
    def __init__(self, username,id):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers+=1
        self.following+=1

    def __str__(self):
        things = []
        for key,value in self.__dict__.items():
            things.append(f"{key} = {value}")
        return str(things)

user_1 = User("BBC", "001")
user_2 = User("BBN", "002")

def update():
    print(user_1)
    print(user_2)

update()
user_1.follow(user_2)
print("")
update()
