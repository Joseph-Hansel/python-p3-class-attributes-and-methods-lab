class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        self.genre_counter(self.genre)
        self.artist_counter(self.artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls,genre):
        Song.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        Song.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre,count):
        Song.genre_count.update({f"{genre}": count})

    @classmethod
    def add_to_artist_count(cls,artist,count):
        Song.artist_count.update({f"{artist}": count})

    def genre_counter(self,genre):
        keys = []
        for key in Song.genre_count:
            keys.append(key)
        if genre in keys:
            Song.genre_count[f"{genre}"] += 1
        else:
            self.add_to_genre_count(genre,1)

    def artist_counter(self,artist):
        keys = []
        for key in Song.artist_count:
            keys.append(key)
        if artist in keys:
            Song.artist_count[f"{artist}"] += 1
        else:
            self.add_to_artist_count(artist,1)