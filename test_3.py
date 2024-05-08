class Track:
    def __init__(self, title, duration, artist, album, year, time_play = 0.0):
        self.__title = title
        self.__duration = duration
        self.__artist = artist
        self.__album = album
        self.__year = year
        self.__playing = False
        self.__time_play = time_play



class Album:
    def __init__(self, title, artist, year):
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__tracks = []

    def add_track(self, track):
        self.__tracks.append(track)

    def play_all_tracks(self):
        for track in self.__tracks:
            track.play()

# Пример использования:
track1 = Track("Song 1", "3:45", "Artist 1", "Album A", 2021)
track2 = Track("Song 2", "4:20", "Artist 1", "Album A", 2021)

album1 = Album("Album A", "Artist 1", 2021)
album1.add_track(track1)
album1.add_track(track2)

album1.play_all_tracks()