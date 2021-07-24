class Student:

    def __init__(self, name, major, gpa, is_on_probation=False):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa > 4.5:
            return True
        else:
            return False
