from flask import Flask, make_response, jsonify, request

app = Flask(__name__)


@app.get('/')
def home():
    # lambda functions
    # funtions that does not have name
    (lambda x, y: x + y)(4, 7)
    seq = [1, 3, 5, 3, 5]
    print(list(map(lambda x: x * 2, seq)))
    print([i * 2 for i in seq])
    dict_comp()
    return 'welcome to Flask'


def add(a, b):
    return a + b

def dict_comp():
    users = [
        (1, "Rob", "password"),
        (2, "Mob", "mob12312")
    ]

    users_mapping = {user[1]: user for user in users}
    print(users_mapping)
    
    id, username, password = users_mapping["Rob"]
    print(id, username, password)


class Student:
    def __init__(self):
        self.name = None
        self.age = None
        self.email = None

    def is_legal_to_drink(self):
        if self.age > 18:
            return True
        else:
            False

    def __str__(self):
        return f"""name: {self.name}\nage: {self.age}\nemail: {self.email}"""


student = Student()
student.name = "Shashi"
student.age = 29
student.email = "skujur871@gmail.com"
print(student.__dict__)

@app.get('/student')
def student():
    st1 = Student()
    st1.name = "Bhushan"
    st1.age = 29
    st1.email = "bhushanDrinker@gmail.com"

    is_eligible = st1.is_legal_to_drink()
    print(is_eligible)
    print()
    return st1.__dict__