import statistics as stat

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
    
    def _middle_grade(self):
        result = []
        all_grades = [self.grades[course] for course in self.grades.keys()]
        for grades in all_grades:
            for grade in grades:
                result.append(grade)
        return stat.mean(result)
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за д/з: {self._middle_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        if self._middle_grade() < other._middle_grade():
            return(f'Средняя оценка за д/з у {self.name} меньше чем у {other.name}')
        else:
            return(f'Средняя оценка за д/з у {self.name} больше чем у {other.name}')    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._middle_grade()}'

    def _middle_grade(self):
        result = []
        all_grades = [self.grades[course] for course in self.grades.keys()]
        for grades in all_grades:
            for grade in grades:
                result.append(grade)
        return stat.mean(result)
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        if self._middle_grade() < other._middle_grade():
            return(f'Средняя оценка за лекции у {self.name} {self.surname} меньше чем у {other.name} {other.surname}')
        else:
            return(f'Средняя оценка за лекции у {self.name} {self.surname} больше чем у {other.name} {other.surname}')    
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def course_average(list_of_persons, course):
    result = []
    for person in list_of_persons:
        for course_name in person.grades:
            if course_name.lower() == course.lower():
                for grade in person.grades[course]:
                    result.append(grade)
    return stat.mean(result)

student_1 = Student('Мэри', 'Поппинс', 'ж')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Java']

student_2 = Student('Гарри', 'Поттер', 'м')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['HTML, CSS']

list_of_students = [student_1, student_2]

mentor_1 = Mentor('Нина', 'Ни')
mentor_1.courses_attached += ['Python']

mentor_2 = Mentor('Гога', 'Го')
mentor_2.courses_attached += ['Python']

lecturer_1 = Lecturer('Юрий', 'Юр')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Дарья', 'Да')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

list_of_lecturers = [lecturer_1, lecturer_2]

student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_2, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_2, 'Git', 7)

student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 6)
student_2.rate_lecturer(lecturer_1, 'Git', 8)
student_2.rate_lecturer(lecturer_2, 'Git', 10)

reviewer_1 = Reviewer('Джек', 'Джонсон')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Джон', 'Джексон')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Git', 9)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_1, 'Git', 6)
reviewer_2.rate_hw(student_2, 'Git', 10)

print(f'Проверяющие:\n{reviewer_1}\n{reviewer_2}')

print(f'\nЛекторы:\n{lecturer_1}\n{lecturer_2}')

print(f'\nСтуденты:\n{student_1}\n{student_2}')

print(student_2 > student_1)

print(lecturer_1 > lecturer_2)

print(f'Средняя оценка за д/з среди студентов на курсе Python: {course_average(list_of_students, "Python")}')

print(f'Средняя оценка за д/з среди студентов на курсе Git: {course_average(list_of_students, "Git")}')

print(f'Средняя оценка за лекции среди преподавателей на курсе Python: {course_average(list_of_lecturers, "Python")}')

print(f'Средняя оценка за лекции среди преподавателей на курсе Git: {course_average(list_of_lecturers, "Git")}')