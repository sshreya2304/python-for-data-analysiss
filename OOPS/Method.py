class Student:
    def __init__(self, fullname):
        self.name = fullname

    def hello(self):
        print("HEllo", self.name)

s1 = Student("Shreya")
s1.hello()

print(s1.name)
