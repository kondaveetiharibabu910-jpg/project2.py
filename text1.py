class student:
    def __init__(self, name, age, branch, college,city):
        self.name = name
        self.age = age
        self.branch = branch
        self.college = college
        self.city = city
    def display(self):
        print(self,"name", "age", "branch", "college", "city")
c1 = student("hari", 23, "aiml","nri","guntur")
c2 = student("babu", 24, "cse","cect","vij")
print(c1.__dict__) 
print(c2.__dict__)           