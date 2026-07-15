class student:
    def __init__(self,name, branch,id,rollno):
        self.name = name 
        self.branch = branch
        self.id = id
        self.rollno = rollno
    def display(self):
        print(self, "name", "branch", "id", "rollno")


class college(student):
    def __init__(self, name, branch, id, rollno,city,grade):
        super().__init__(name, branch,id ,rollno)
        self.city = city
        self.grade = grade
    def display(self):
        return super().display()
c1 = college("hari", "aiml", 123,12345,"guntur","A+")
c2 = college("siva", "cse",4321,456,"ullagallu","b+")
print(c1.__dict__)
print(c2.__dict__)