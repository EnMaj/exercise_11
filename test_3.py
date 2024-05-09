# -*- coding: windows-1251 -*-
import time
from inputimeout import inputimeout
from threading import Timer


class Track:
    def __init__(self, title, duration, artist, album, year, current_time=0.0):
        self.__title = title
        self.__min, self.__sec = duration.split(':')
        self.__duration = float(self.__min) * 60 + float(self.__sec)
        self.__artist = artist
        self.__album = album
        self.__year = year
        self.__playing = False
        self.__current_time = current_time
        self.__end_command = None

    def play(self):
        self.__playing = True
        begin_time = time.time()
        while self.__playing:
            print(self.__title)
            print('command?')
            t = Timer(self.__duration - self.__current_time, lambda: self.stop())
            t.start()
            self.__end_command = input()
            t.cancel()
            if self.__end_command == 'pause' and self.__playing:
                self.pause(begin_time)
            elif self.__end_command == 'stop' and self.__playing:
                self.stop()
            elif self.__end_command == 'next' and self.__playing:
                self.stop()
            elif self.__end_command == 'past' and self.__playing:
                self.stop()
            '''
            command = inputimeout(prompt='Введите команду: ', timeout=(self.__duration - self.__current_time))
            try:
                if command == 'pause':
                    print('pause')
                    end_time = now_time - time.time()
                    self.__current_time = self.__duration - end_time
                    self.__playing = False

            except:
                self.__playing = False
                self.__current_time = 0.0
                '''

    def pause(self, begin_time):
        print('pause')
        end_time = time.time() - begin_time
        self.__current_time = self.__duration - end_time
        self.__playing = False

    def stop(self):
        print('stop')
        self.__playing = False
        self.__current_time = 0.0

    @property
    def title(self):
        return self.__title

    @property
    def duration(self):
        return self.__duration

    @property
    def current_time(self):
        return self.__current_time

    @current_time.setter
    def current_time(self, current_time):
        self.__current_time = current_time

    @property
    def playing(self):
        return self.__playing

    @playing.setter
    def playing(self, playing):
        self.__playing = playing

    @property
    def end_command(self):
        return self.__end_command


class Album:
    def __init__(self, title, artist, year):
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__tracks = []
        self.__index_end_track = 0

    def add_track(self, track):
        self.__tracks.append(track)

    def del_track(self, track):
        self.__tracks.remove(track)

    def play_album(self):
        for i in range(self.__index_end_track, len(self.__tracks)):
            self.__tracks[i].play()
            if not self.__tracks[i].playing:
                self.__index_end_track = i
            if self.__tracks[i].end_command == 'pause':
                break
            if self.__tracks[i].end_command == 'stop':
                self.__index_end_track = 0
                break
            if self.__tracks[i].end_command == 'past':
                self.__index_end_track -= 1
                i -= 1

    @property
    def tracks(self):
        return self.__tracks


track1 = Track("Song 1", "0:5", "Artist 1", "Album A", 2021)
track2 = Track("Song 2", "0:10", "Artist 1", "Album A", 2021)

album1 = Album("Album A", "Artist 1", 2021)
album1.add_track(track1)
album1.add_track(track2)
i = 0
album1.play_album()
