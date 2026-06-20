class Student : 
    """A class to represent a student with their name and grades in different subjects."""
    def __init__(self,name: str,grades: dict):
        self.name=name
        self.grades=grades
        print(f"Student {self.name} created with grades: {self.grades}")

    def add_grade(self, subj_name, grade):
        """Add a grade for a specific subject."""
        self.grades[subj_name] = grade
        print(f"subject Name added: {subj_name} with grade {grade} For student {self.name}")

    def get_average(self):
        """Calculate and print the average grade for all Subjects."""
        average = sum(self.grades.values())/len(self.grades)
        print(f"The average of the result for student {self.name} is : {average}")

    def print_info(self):
        """Print the student's Details including name, grades, and average."""
        print(f"The student name : {self.name}")
        print(f"The grades in subjects is : {self.grades}")
        print(f"The average of the result is : {sum(self.grades.values())/len(self.grades)}")
#Creating two instances of the Student class and testing the methods
s1=Student("Ahmed",{"Math":90,"Science":85})
s1.add_grade("English", 88)
print("-"*20)

s2=Student("Sara",{"Math":95,"Science":92})
s2.add_grade("English", 90)
print("-"*20)

#getting the average of the grades for both students
s1.get_average()
s2.get_average()
print("-"*20)

#showing the information of both students
s1.print_info()
print("-"*20)
s2.print_info()