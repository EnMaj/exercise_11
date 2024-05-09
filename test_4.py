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
        print(f'���������� ������ {self.__number} �� ���� �������: ')
        for key, value in schedules[schedule].group_schedule.items():
            print(f'{key}: ')
            if value != None:
                for key_1, value_1 in days[value].day_lessons.items():
                    if value_1 != None:
                        print(f'{key_1}: {lessons[value_1].subject} {lessons[value_1].teacher} {lessons[value_1].room}')
                    else:
                        print(f'{key_1}: ��� ���')
            else:
                print('��������')

    def print_schedule_data(self,lessons, days, schedules, data):
        ru_data = {
            'Monday': '�����������',
            'Tuesday': '�������',
            'Wednesday': '�����',
            'Thursday': '�������',
            'Friday': '�������',
            'Saturday': '�������',
            'Sunday': '�����������',
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
            if key == '����':
                id = i['����']['ID']
                subject = i['����']['�������']
                teacher = i['����']['�������������']
                room = i['����']['���������']
                lessons[id] = Lesson(id, subject, teacher, room)

    for i in dictionary:
        for key in i:
            if key == '����':
                id = i['����']['ID']
                day_lessons = i['����']
                days[id] = Day(id, day_lessons)

    for i in dictionary:
        for key in i:
            if key == '����������':
                id = i['����������']['ID']
                group_schedule = i['����������']
                schedules[id] = Schedule(id, group_schedule)

    for i in dictionary:
        for key in i:
            if key == '������':
                id = i['������']['ID']
                schedule = i['������']['����������']
                groups[id] = Group(id, schedule)
'''print('lessons', lessons)
print('days', days)
print('schedules', schedules)
print('groups', groups)'''
groups[22704].print_group_schedule(lessons, days, schedules)
