class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        sum_grades = 0
        for course in self.grades:
            sum_grades += sum(self.grades[course])
        return sum_grades / len(self.grades[course])

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.avg_grade(), 1)}\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'


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
        sum_grades = 0
        for course in self.grades:
            sum_grades += sum(self.grades[course])
        return sum_grades / len(self.grades[course])

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.avg_grade(), 1)}'

class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached=[]):
        super().__init__(name, surname, courses_attached)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)

best_lecturer = Lecturer('John', 'Doe')
best_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(best_lecturer, 'Python', 9)
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 10)

print(cool_reviewer)
print()
print(best_student.grades)
print()
print(best_lecturer.grades)
print()
print(best_lecturer)
print()
print(best_student)