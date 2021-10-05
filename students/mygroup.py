groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП", "Информатика"],
        "marks": [4, 4, 4, 5]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП", "АиГ"],
        "marks": [5, 5, 5, 4]
    },
    {
        "name": "Александр",
        "surname": "Сидоров",
        "exams": ["Информатика", "АиГ", "КТП"],
        "marks": [5, 3, 4]
    },
    {
        "name": "Владимир",
        "surname": "Пушкин",
        "exams": ["История", "ЭЭиС"],
        "marks": [4, 5]
    }
]


def filter_students(students, user_score):
    new_students = []
    for student in students:
        # делим сумму оценок на число оценок для получения среднего и сравниваем с переданным баллом
        if sum(student["marks"]) / len(student["marks"]) > user_score:
            new_students.append(student)
    return new_students


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(40), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(40),
              str(student["marks"]).ljust(20))


score = float(input("Введите балл: "))
filtered_students = filter_students(groupmates, score)
print_students(filtered_students)
