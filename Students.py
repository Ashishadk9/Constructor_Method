class Student:
    def __init__(self, name, maths, science, english):
        self.name = name
        self.maths = maths
        self.science = science
        self.english = english

    def get_last_name(self):
        # Split the name and return the last part
        return self.name.split()[-1]

    def get_average_marks(self):
        # Calculate the average of the three subjects
        return (self.maths + self.science + self.english) / 3


# Example 
student1 = Student("John son", 85, 90, 80)
print("Last Name:", student1.get_last_name())          # Output: Johnson
print("Average Marks:", student1.get_average_marks())  # Output: 85.0
