class Lecturer:

    def __init__(self, name, academic_degree):
        self.__name = name
        self.__academic_degree = academic_degree


class Subject:

    def __init__(self, name, lecturer):
        self.__name = name
        self.__lecturer = lecturer


class Audience:

    def __init__(self, floor, number):
        self.__floor = floor
        self.__number = number
        self.__block = number//100


class Lesson:
    def __init__(self, day, time):
        self.__day = day
        self.__time = time


class Schedule:
    def __init__(self):
        self.__scheudule = []
        for i in range(7):





