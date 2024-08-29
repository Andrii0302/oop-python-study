from random import choice

class Student():
    eductaional='Udemy'
    def __init__(self, name, age=22):
        self.name = name
        self.age = age
    def greet(self):
        greetings=["Hi, I'm {}", "Hello, I'm {}", "Howdy, I'm {}"]
        greeting=choice(greetings)
        return greeting.format(self.name)

def class_create(names):
    return [Student(name) for name in names]
if __name__ == '__main__':
    name= ['Mandy', 'Andy', 'Joe', 'Jim']
    for stud in class_create(name):
        print(stud.greet())