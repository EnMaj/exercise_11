# -*- coding: windows-1251 -*-
import json
import datetime


class Lesson:

    def __init__(self, id, subject, teacher, room):
        self.__id = id
        self.__subject = subject
        self.__teacher = teacher
        self.__room = room

    @property
    def subject(self):
        return self.__subject

    @property
    def teacher(self):
        return self.__teacher

    @property
    def room(self):
        return self.__room


class Day:

    def __init__(self, id, day_lessons):
        self.__id = id
        del day_lessons['ID']
        self.__day_lessons = day_lessons

    @property
    def day_lessons(self):
        return self.__day_lessons


class Schedule:
    def __init__(self, id, group_schedule):
        self.__id = id
        del group_schedule['ID']
        self.__group_schedule = group_schedule

    @property
    def group_schedule(self):
        return self.__group_schedule


class Group:
    def __init__(self, number, schedule):
        self.__number = number
        self.__shedule = schedule

    def print_group_schedule(self, lessons, days, schedules):
        print(f'Расписание группы {self.__number} на этот семестр: ')
        for key, value in schedules[schedule].group_schedule.items():
            print(f'{key}: ')
            if value != None:
                for key_1, value_1 in days[value].day_lessons.items():
                    if value_1 != None:
                        print(f'{key_1}: {lessons[value_1].subject} {lessons[value_1].teacher} {lessons[value_1].room}')
                    else:
                        print(f'{key_1}: нет пар')
            else:
                print('Выходной')

    def print_schedule_data(self,lessons, days, schedules, data):
        ru_data = {
            'Monday': 'Понедельник',
            'Tuesday': 'Вторник',
            'Wednesday': 'Среда',
            'Thursday': 'Четверг',
            'Friday': 'Пятница',
            'Saturday': 'Суббота',
            'Sunday': 'Воскресенье',
        }
        day = data[:2]
        month = data[2:4]


with open('file.json', 'r') as file_json:
    dictionary = json.load(file_json)
    lessons = dict()
    days = dict()
    schedules = dict()
    groups = dict()
    for i in dictionary:
        for key in i:
            if key == 'Пара':
                id = i['Пара']['ID']
                subject = i['Пара']['Предмет']
                teacher = i['Пара']['Преподаватель']
                room = i['Пара']['Аудитория']
                lessons[id] = Lesson(id, subject, teacher, room)

    for i in dictionary:
        for key in i:
            if key == 'День':
                id = i['День']['ID']
                day_lessons = i['День']
                days[id] = Day(id, day_lessons)

    for i in dictionary:
        for key in i:
            if key == 'Расписание':
                id = i['Расписание']['ID']
                group_schedule = i['Расписание']
                schedules[id] = Schedule(id, group_schedule)

    for i in dictionary:
        for key in i:
            if key == 'Группа':
                id = i['Группа']['ID']
                schedule = i['Группа']['Расписание']
                groups[id] = Group(id, schedule)
'''print('lessons', lessons)
print('days', days)
print('schedules', schedules)
print('groups', groups)'''
groups[22704].print_group_schedule(lessons, days, schedules)
