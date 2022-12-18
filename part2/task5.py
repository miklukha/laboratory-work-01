# The class GROUP contains a sequence of instances of the class STUDENT.
# The class STUDENT contains the student's name, surname, record book number and grades.
# Determine the required attributes-data and attributes-methods in classes GROUP and STUDENT.
# Find the average score of each student.
# Output to the standard output stream the five students with the highest average score.
# Assume that there can be no more than 20 students in a group, as well as students with the same name and surname.

class Group:
    students = []

    def __init__(self, group_name):
        self.group_name = group_name

    def add_student(self, student):
        if len(self.students) >= 20:
            return "The group can contain only 20 students"
        else:
            if len(self.students) != 0:
                for element in self.students:
                    if element.firstname == student.firstname and element.surname == student.surname:
                        return f"Student: {student.firstname} {student.surname} already exist"
                    else:
                        continue
            self.students.append(student)
            return f"Student: {student.firstname} {student.surname} has been added"

    def get_students(self):
        for student in self.students:
            print(f"Name: {student.firstname} {student.surname}\n"
                  f"Average score: {student.average_score}\n")
        return self.students

    def get_the_best_students(self):
        sorted_students = sorted(self.students, key=lambda x: x.average_score, reverse=True)

        for i in range(0, 5):
            print(f"Name: {sorted_students[i].firstname} {sorted_students[i].surname}\n"
                  f"Average score: {sorted_students[i].average_score}\n")


class Student:
    average_score = 0

    def __init__(self, firstname, surname, record_book_number, grades={}):
        self.firstname = firstname
        self.surname = surname
        self.record_book_number = record_book_number
        self.grades = grades

    def count_average_score(self):
        grades = self.grades.values()

        for grade in grades:
            self.average_score += grade
        self.average_score /= len(grades)

        return self.average_score


student1 = Student('Igor', 'Vecherya', '122489', {'OOP': 4, 'DataBase': 4, 'The theory of probabilidad': 3, 'English': 5})
student1.count_average_score()
student2 = Student('Olena', 'Vasylenko', '122490', {'OOP': 3, 'DataBase': 4, 'The theory of probabilidad': 3, 'English': 3})
student2.count_average_score()
student3 = Student('Vasyl', 'Openko', '122491', {'OOP': 4, 'DataBase': 5, 'The theory of probabilidad': 5, 'English': 5})
student3.count_average_score()
student4 = Student('Anton', 'Ponko', '122492', {'OOP': 5, 'DataBase': 5, 'The theory of probabilidad': 3, 'English': 3})
student4.count_average_score()
student5 = Student('Olena', 'Bilenko', '122493', {'OOP': 4, 'DataBase': 3, 'The theory of probabilidad': 3, 'English': 5})
student5.count_average_score()
student6 = Student('Anna', 'Lasarenko', '122494', {'OOP': 3, 'DataBase': 4, 'The theory of probabilidad': 5, 'English': 3})
student6.count_average_score()
student7 = Student('Sergiy', 'Zavadsky', '122495', {'OOP': 4, 'DataBase': 4, 'The theory of probabilidad': 5, 'English': 5})
student7.count_average_score()

group = Group('TV-z11')
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)
group.add_student(student4)
group.add_student(student5)
group.add_student(student6)
group.add_student(student7)
# group.get_students()
group.get_the_best_students()
