class Student:
    "Класс описывает студентов Нетологии."
    def __init__(self, name, surname, gender):
        "Инициализация"
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        "Функция для оценки лекторов студентами"
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]


    def __str__(self):
        "Функция для вывода данных студента"
        result = f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания:{Lecturer.avg_grade(self)}\n" \
                 f"Курсы в процессе изучения: {', '.join(i for i in self.courses_in_progress)}\n" \
                 f"Завершенные курсы: {self.finished_courses}"
        return result
        
class Mentor:
    "Материнский класс для преподавателей"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Lecturer(Mentor):
    "Дочерний класс описывающий лекторов"
    def __init__(self, name, surname):
        super().__init__(name,  surname)
        self.grades = {}
    
    def avg_grade(self):
        "Среднее значение по выставленным оценкам"
        summa = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                count += 1
                summa += grade
        avg = round((summa / count),1)
        return avg


    def __str__(self):
        result = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.avg_grade()}'
        return result
    
class Reviewer(Mentor):
    "Дочерний класс для описания ревьюеров"
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
    "Функция сранения студентов и лекторов"
    if Lecturer.avg_grade(student) > Lecturer.avg_grade(lecturer):
        result = f'Средняя оценка студента больше, чем лектора'
    else:
        result = f'Средняя оценка лектора больше, чем студента'
    return result

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Введение в программирование']
some_student.finished_courses += ['SQL']
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Введение в программирование']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Введение в программирование', 10)
some_reviewer.rate_hw(some_student, 'Python', 2)

some_lecturer = Lecturer('Ivan', 'Ivanov',)
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Введение в программирование']

some_student.rate_lecturer(some_lecturer, 'Python', 9)
some_student.rate_lecturer(some_lecturer, 'Python', 5)
 
# print(some_student.grades)
# print(some_lecturer.grades)
# print(some_reviewer)
print(some_lecturer)
print(some_student)
print(compare_student_lecturer(some_student,some_lecturer))
