class Student():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (
                self.courses_in_progress or self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {sr_grade(self.grades)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return output


class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sr_grade(self.grades)}'
        return output


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output


def sr_grade(gr):
    k = 0
    s = 0
    for cour in gr.keys():
        for grad in gr[cour]:
            k += 1
            s += grad
    return s / k


def sr_students(st, course):
    s = 0
    k = 0
    for stud in st:
        for grad in stud.grades.get(course):
            k += 1
            s += grad
    return s / k


def sr_lecturer(lect, course):
    s = 0
    k = 0
    for lec in lect:
        for grad in lec.grades.get(course):
            k += 1
            s += grad
    return s / k


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
b_student = Student('Ru', 'man', 'your_gender')
b_student.courses_in_progress += ['Python']
bt = Student('Ry', 'Emn', 'your_gender')
bt.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(b_student, 'Python', 10)
cool_mentor.rate_hw(bt, 'Python', 7)
cool_mentor.rate_hw(b_student, 'Python', 2)
cool_mentor.rate_hw(bt, 'Python', 6)

b_lector = Lecturer('Gena', 'Hut')
b_lector.courses_attached += ['Python']
best_student.rate_lec(b_lector, 'Python', 5)
best_student.rate_lec(b_lector, 'Python', 17)

print(b_lector)