class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def middle_grade(self):
        new_list = []
        for grades in self.grades.values():
            new_list.extend(grades)
        result = sum(new_list) / len(new_list)
        return round(result, 1)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.middle_grade() < other.middle_grade()
        else:    
            return f'В сравнении не все студенты'
        
    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and self.finished_courses:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.middle_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
            f'Оценки: {self.grades}\n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def middle_grade(self):
        new_list = []
        for grades in self.grades.values():
            new_list.extend(grades)
        result = sum(new_list) / len(new_list)
        return round(result, 1)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.middle_grade() < other.middle_grade()
        else:
            return f'В сравнении не все преподаватели'
            
    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Ведет лекции по предметам: {", ".join(self.courses_attached)}\n'
            f'Средняя оценка за лекции: {self.middle_grade()}\n'
            f'Оценки: {self.grades}\n')


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
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Проверяет ДЗ по предметам: {", ".join(self.courses_attached)}\n')


# Студенты
student_one = Student('Алексей', 'Крылов', 'мужской')
student_one.courses_in_progress += ['Python', 'SQL']
student_one.finished_courses += ['GIT', 'API']

student_two = Student('Марина', 'Иванова', 'женский')
student_two.courses_in_progress += ['GIT', 'API']
student_two.finished_courses += ['Python', 'SQL']

#Лекторы
lecturer_one = Lecturer('Олег', 'Булыгин')
lecturer_one.courses_attached += ['Python', 'SQL']
student_two.rate_lecture(lecturer_one, 'Python', 10)
student_two.rate_lecture(lecturer_one, 'Python', 9)
student_two.rate_lecture(lecturer_one, 'SQL', 8)
student_two.rate_lecture(lecturer_one, 'Python', 10)

lecturer_two = Lecturer('Иван', 'Батистов')
lecturer_two.courses_attached += ['GIT', 'API']
student_one.rate_lecture(lecturer_two, 'GIT', 7)
student_one.rate_lecture(lecturer_two, 'API', 5)

#Проверяющие
reviewer_one = Reviewer('Андрей', 'Васильев')
reviewer_one.courses_attached += ['Python', 'SQL']
reviewer_one.rate_hw(student_one, 'Python', 10)
reviewer_one.rate_hw(student_one, 'Python', 8)
reviewer_one.rate_hw(student_one, 'Python', 8)
reviewer_one.rate_hw(student_one, 'SQL', 8)

reviewer_two = Reviewer('Владимир', 'Петрович')
reviewer_two.courses_attached += ['GIT', 'API']
reviewer_two.rate_hw(student_two, 'GIT', 9)
reviewer_two.rate_hw(student_two, 'API', 7)

list_student = [student_one,student_two]
list_lecturer = [lecturer_one, lecturer_two]

# Определяем среднюю оченку за предмет у студентов
def middle_grade_courses_student(list_student, courses):
    list_grade = []
    for student in list_student:
        for lesson in student.grades.keys():
            if lesson == courses:
                list_grade.extend(student.grades[lesson])
    return round(sum(list_grade)/len(list_grade),1) 

# Определяем среднюю оченку за предмет у лекторов
def middle_grade_courses_lecturer(list_lecturer, courses):
    list_grade = []
    for lecturer in list_lecturer:
        for lesson in lecturer.grades.keys():
            if lesson == courses:
                list_grade.extend(lecturer.grades[lesson])
    return round(sum(list_grade)/len(list_grade),1) 

print(lecturer_one)
print(lecturer_two)
print(student_one)
print(student_two)
print(reviewer_one)
print(reviewer_two)
print(lecturer_one < lecturer_two)
print(student_one > student_two)
print (middle_grade_courses_student(list_student,'Python'))
print (middle_grade_courses_lecturer(list_lecturer,'Python')) 