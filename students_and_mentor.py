class Student:
    """Класс описывает студентов Нетологии."""
    def __init__(self, name, surname, gender):
        "Инициализация"
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        """Функция для оценки лекторов студентами"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def __str__(self):
        """Функция для вывода данных студента"""
        result = f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания:{Lecturer.avg_grade(self)}\n" \
                 f"Курсы в процессе изучения: {', '.join(i for i in self.courses_in_progress)}\n" \
                 f"Завершенные курсы: {', '.join(i for i in self.finished_courses)}"
        return result


class Mentor:
    """Материнский класс для преподавателей"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Lecturer(Mentor):
    """Дочерний класс описывающий лекторов"""
    def __init__(self, name, surname):
        super().__init__(name,  surname)
        self.grades = {}
    
    def avg_grade(self):
        """Среднее значение по выставленным оценкам"""
        summa = 0
        count_grades = 0
        for grades in self.grades.values():
            for grade in grades:
                count_grades += 1
                summa += grade
        avg = round((summa / count_grades),1)
        return avg

    def __str__(self):
        result = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.avg_grade()}'
        return result


class Reviewer(Mentor):
    """Дочерний класс для описания ревьюеров"""
    def rate_hw(self, student, course, grade):
        "Функция для оценки студентов лекторами"
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


def compare_student_lecturer(student, lecturer):
    """Функция сранения студентов и лекторов"""
    if Lecturer.avg_grade(student) > Lecturer.avg_grade(lecturer):
        result = f'Средняя оценка студента больше, чем лектора'
    else:
        result = f'Средняя оценка лектора больше, чем студента'
    return result


first_student = Student('Иван', 'Петров', 'м')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Введение в программирование']
first_student.finished_courses += ['SQL']
second_student = Student('Вика', 'Тевс', 'ж')
second_student.courses_in_progress += ['SQL']
second_student.courses_in_progress += ['Введение в программирование']
second_student.finished_courses += ['Python']

 
first_reviewer = Reviewer('Виктор', 'Симонов')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Введение в программирование']
second_reviewer = Reviewer('Владимир', 'Путинов')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['SQL']

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Введение в программирование', 10)
first_reviewer.rate_hw(first_student, 'Введение в программирование', 6)
first_reviewer.rate_hw(first_student, 'Python', 2)
second_reviewer.rate_hw(first_student, 'SQL', 5)
second_reviewer.rate_hw(second_student, 'SQL', 8)
second_reviewer.rate_hw(first_student, 'Python', 9)

first_lecturer = Lecturer('Яков', 'Цой',)
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Введение в программирование']
second_lecturer = Lecturer('Богдан', 'Веселый',)
second_lecturer.courses_attached += ['SQL']
second_lecturer.courses_attached += ['Введение в программирование']

first_student.rate_lecturer(first_lecturer, 'Python', 9)
first_student.rate_lecturer(first_lecturer, 'Введение в программирование', 8)
second_student.rate_lecturer(second_lecturer, 'SQL', 10)
second_student.rate_lecturer(first_lecturer, 'Введение в программирование', 5)
second_student.rate_lecturer(second_lecturer, 'Введение в программирование', 8)

list_of_students = [first_student, second_student]
list_of_lecturer = [first_lecturer,second_lecturer]


def avg_between_courses(person, course_name):
    """Функция для нахождения средней оценки по курсу"""
    summa = 0
    for grade in person.grades[course_name]:
        summa += grade
    avg_rate = summa / len(person.grades[course_name])
    return avg_rate


def avg_all(people_list, course_name):
    """Средняя оценка по курсам среди всех студентов или лекторов"""
    avg_person = 0
    people_counter = 0
    for people in people_list:
        if course_name in people.grades:
            avg_person += avg_between_courses(people, course_name)
            people_counter += 1
    all_student_avg = f'Средняя оценка по курсу {course_name} равна: {round((avg_person / people_counter), 1)}'
    return all_student_avg


print(avg_all(list_of_students, 'Python'))
print(avg_all(list_of_lecturer, 'Введение в программирование'))

# print(some_student.grades)
# print(some_lecturer.grades)
# print(some_reviewer)
# print(first_lecturer)
# print(first_student)
# print(compare_student_lecturer(first_student,first_lecturer))
