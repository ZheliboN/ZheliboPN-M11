import inspect


def introspection_info(obj):
    info_obj = dict()
    info_obj['type'] = str(type(obj).__name__)
    info_obj['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info_obj['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    modul = inspect.getmodule(obj)
    if modul is None:
        info_obj['module'] = obj.__class__.__module__
    else:
        info_obj['module'] = modul.__name__
    return info_obj


class Student:
    def __init__(self, name_student, age_student):
        self.FIO = name_student
        self.Age = age_student

    def __str__(self):
        student_info = f'Студент: {self.FIO}, возраст: {self.Age}'
        return student_info


s1 = Student('Иванов Иван Иванович',  19)
number_info1 = introspection_info(42)
print(number_info1)
number_info2 = introspection_info('42')
print(number_info2)
number_info3 = introspection_info(s1)
print(number_info3)
