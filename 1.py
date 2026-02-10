class Academic:
    def get_academic_marks(self):

        self.marks = []

        for i in range(1, 5):

            m = float(input(f"Enter score for Subject {i}: "))
            self.marks.append(m)

    def calculate_percentage(self):

        total = sum(self.marks)

        self.percentage = (total / 400) * 100
        return self.percentage

class Sports:
    def get_sports_score(self):
        self.sport_mark = float(input("Enter Sports Score: "))

    def display_sports(self):
        print(f"Sports Score: {self.sport_mark}")

class Student(Academic, Sports):

    def __init__(self, name):

        self.name = name

    def display_result(self):

        print(f"\n--- Student Report: {self.name} ---")

        percentage = self.calculate_percentage()

        print(f"Academic Percentage: {percentage}%")

        self.display_sports()


name = input("Enter Student Name: ")
student_obj = Student(name)
student_obj.get_academic_marks()
student_obj.get_sports_score()
student_obj.display_result()
