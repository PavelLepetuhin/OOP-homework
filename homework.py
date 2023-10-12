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

best_student1 = Student('Имя', 'Фамилия', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Git']
best_student1.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(best_student, 'Git', 10)

cool_reviewer.rate_hw(best_student1, 'Python', 7)
cool_reviewer.rate_hw(best_student1, 'Python', 8)
cool_reviewer.rate_hw(best_student1, 'Python', 9)
cool_reviewer.rate_hw(best_student1, 'Git', 10)
cool_reviewer.rate_hw(best_student1, 'Git', 7)
cool_reviewer.rate_hw(best_student1, 'Git', 10)

best_lecturer = Lecturer('John', 'Doe')
best_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 8)
best_student.rate_lecturer(best_lecturer, 'Python', 8)

print(best_student)
print()
print(best_student1)
print()
print(cool_reviewer)
print()
print(best_lecturer)
print()
print(best_student < best_student1)
print(best_student > best_student1)
print(best_student == best_student1)
