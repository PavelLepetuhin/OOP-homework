import statistics


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
           and course in self.courses_in_progress
           and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def avg_grade(self):
        total_grades = []
        for grade in list(self.grades.values()):
            total_grades += grade
        return statistics.mean(total_grades)

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {round(self.avg_grade(), 1)}\n'
                f'Курсы в процессе обучения: '
                f'{", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname, courses_attached=[]):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached=[]):
        super().__init__(name, surname, courses_attached)
        self.grades = {}

    def avg_grade(self):
        total_grades = []
        for grade in list(self.grades.values()):
            total_grades += grade
        return statistics.mean(total_grades)

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {round(self.avg_grade(), 1)}')


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached=[]):
        super().__init__(name, surname, courses_attached)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
           and course in self.courses_attached
           and course in student.courses_in_progress):
            if course in student.grades.keys():
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student_1 = Student('Имя', 'Фамилия', 'your_gender')
best_student_1.courses_in_progress += ['Python']
best_student_1.courses_in_progress += ['Git']
best_student_1.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(best_student, 'Git', 10)

cool_reviewer.rate_hw(best_student_1, 'Python', 7)
cool_reviewer.rate_hw(best_student_1, 'Python', 8)
cool_reviewer.rate_hw(best_student_1, 'Python', 9)
cool_reviewer.rate_hw(best_student_1, 'Git', 10)
cool_reviewer.rate_hw(best_student_1, 'Git', 7)
cool_reviewer.rate_hw(best_student_1, 'Git', 10)

best_lecturer = Lecturer('John', 'Doe')
best_lecturer.courses_attached += ['Python']

best_lecturer_1 = Lecturer('Jack', 'Smith')
best_lecturer_1.courses_attached += ['Python']

best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 8)
best_student.rate_lecturer(best_lecturer, 'Python', 8)

best_student_1.rate_lecturer(best_lecturer_1, 'Python', 8)
best_student_1.rate_lecturer(best_lecturer_1, 'Python', 8)
best_student_1.rate_lecturer(best_lecturer_1, 'Python', 8)

print(best_student)
print()
print(best_student_1)
print()
print(cool_reviewer)
print()
print(best_lecturer)
print()
print(best_student < best_student_1)
print(best_student > best_student_1)
print(best_student == best_student_1)
print()
print(best_lecturer < best_lecturer_1)
print(best_lecturer > best_lecturer_1)
print(best_lecturer == best_lecturer_1)
print()

list_students = [best_student, best_student_1]

def stud_avg_grade(list_students, course_name):
    total_grades = []
    for student in list_students:
        total_grades += student.grades[course_name]
    return (f' Средняя оценка всех студентов на курсе {course_name}:'
            f' {round(statistics.mean(total_grades))}')

print(stud_avg_grade(list_students, 'Python'))
print(stud_avg_grade(list_students, 'Git'))


def lect_avg_grade(list_lecturers, course_name):
    total_grades = []
    for lecturer in list_lecturers:
        total_grades += lecturer.grades[course_name]
    return (f' Средняя оценка всех лекторов на курсе {course_name}:'
            f' {round(statistics.mean(total_grades), 1)}')

print(lect_avg_grade([best_lecturer, best_lecturer_1], 'Python'))