"""
Student Class

1. implement a constructor to initialize the values of four properties: name, phy, chem, bio
2. implement a method total_obtained in the student class that calculates total marks of student
3. Using the total_obtained method, implement another method, percentage, in the student class that calculates
    the percentage of student marks. Assume that the total marks  of each subject are 100. The combined marks or three
    subjects are 300

"""
class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def total_obtained(self):
        return self.phy + self.chem + self.bio


    def percentage(self):
        total_obtained = self.total_obtained()
        return round((total_obtained / 300) * 100)


student = Student("victor", 100, 90, 70)

student_two = Student("Michael", 90, 80, 56)

print(student.phy)
print(student.total_obtained())
print(student.percentage())

print(student_two.percentage())
