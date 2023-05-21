from flask import Flask, make_response, jsonify, request, render_template
from random import choice, randint
from string import ascii_letters, punctuation
from device import Printer

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
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def is_legal_to_drink(self):
        if self.age > 18:
            return True
        else:
            False

    def __str__(self):
        return f"""name: {self.name}\nage: {self.age}\nemail: {self.email}"""

    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")

    @staticmethod
    def static_method() -> None:
        """static method"""
        print("called static method")

    # factory method
    @classmethod
    def create_student(cls, name: str, age) -> object:
        """this class method creates Student Object"""
        random_str = ""
        for _ in range(4):
            random_str += choice(ascii_letters)
        assign_email = f"{name.replace(' ', '')}{choice(punctuation)}{age * randint(1, 8)}{random_str}@mymail.com"
        return Student(name, age, assign_email)


# student = Student()
# student.name = "Shashi"
# student.age = 29
# student.email = "skujur871@gmail.com"
# print(student.__dict__)

@app.get('/student')
def student():
    # st1 = Student()
    # st1.name = "Bhushan"
    # st1.age = 29
    # st1.email = "bhushanDrinker@gmail.com"

    # is_eligible = st1.is_legal_to_drink()
    # print(is_eligible)
    # st1.class_method()
    Student.static_method()

    st2 = Student.createStudent("Shashi Bhagat", 29)
    print(st2)

    printer = Printer("Printer", "USB", capacity=400)
    printer.print_pages(3, ['Im going to print', "this is feeling awesome"])
    print(printer)
    printer.print_pages(3, ['new data to print', "this is data is old 😘"])
    print(printer)
    printer.disconnect()
    printer.print_pages(3, ['new data to print', "this is data is old 😘"])
    return st2.__dict__


@app.get('/login')
def login():
    return render_template('login.html', title="login here")