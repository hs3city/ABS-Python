# import requests
#
# response = requests.get('https://')
# data = response.json()
# x = 'jakies slowo'
# x = str('jakies slowo')
# x.capitalize()
#
# print(x.replace('slowo', 'cos innego'))

# 1. dane <----- name, age, grade_average
# 2. zachowania
class Teacher:
    def __init__(self, name, age, grade_average):
        self.name = name
        self.age = age
        self.grade_average = grade_average


# class list:
#     def __eq__(self, other):
#         for i in range(len(self)):
#             if self[i] != other[i]:
#                 return False
#             return True


class Student:
    def __init__(self, name, age, grade_average):
        self.name = name
        self.age = age
        self.grade_average = grade_average

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age and self.grade_average == other.grade_average:
            return True
        return False

    def __str__(self):
        return f'{self.name} {self.age}'

    def is_over_18(self):
        if self.age >= 18:
            return True
        else:
            return False

    def is_valedictorian(self):
        if self.grade_average == 100:
            return True
        else:
            return False


class Classroom:
    def __init__(self, students):
        self.students = students

    def get_all_underage_students(self):
        underaged_students = []
        for student in self.students:
            if student.age < 18:
                underaged_students.append(student)
        return underaged_students


student_maciek = Student('Maciek', 18, 88)

polish_students = [
    Student(name="Aleksandra Nowak", age=17, grade_average=81.5),
    Student(name="Michał Kowalski", age=16, grade_average=92.0),
    Student(name="Katarzyna Wiśniewska", age=18, grade_average=78.3),
]

abroad_students = [
    Student(name="John Smith", age=17, grade_average=85.5),
    Student(name="Emily Johnson", age=16, grade_average=92.0),
    Student(name="Michael Williams", age=18, grade_average=78.3),
]


def average_grade(students):
    sum_of_averages = 0
    for student in students:
        sum_of_averages = sum_of_averages + student.grade_average
    return sum_of_averages / len(students)


print(average_grade(polish_students))

average_of_abroad = average_grade(abroad_students)
print(average_of_abroad)


def get_best_student(students):
    best_student = students[0]
    for student in students[1:]:
        if student.grade_average > best_student.grade_average:
            best_student = student
    return best_student


best_of_polish = get_best_student(polish_students)
print(f'Najlepszy student to {best_of_polish}')


def get_worst_student(students):
    worst_student = students[0]
    for student in students[1:100]:
        if student.grade_average < worst_student.grade_average:
            worst_student = student
    return worst_student


worst_of_polish = get_worst_student(polish_students)
print(f'Najgorszy student to {worst_of_polish.name}')


def students_with_name_starting_with(letter, all_students):
    filtered_students = []
    for student in all_students:
        if student.name[0] == letter:
            filtered_students.append(student)
    return filtered_students


polish_classroom = Classroom(polish_students)

underaged_polish = polish_classroom.get_all_underage_students()
for underaged_polish_student in underaged_polish:
    print(underaged_polish_student)


def test_students_with_name_starting_with_A_letter():
    test_students = [
        Student('Paweł', 18, 88),
        Student('Agata', 18, 88),
        Student('Andrzej', 18, 88),
    ]
    expected_students = [
        Student('Agata', 18, 88),
        Student('Andrzej', 18, 88),
    ]

    result = students_with_name_starting_with("A", test_students)

    if result == expected_students:
        print('test A OK')
    else:
        raise Exception("test A nie przechodzi")


test_students_with_name_starting_with_A_letter()