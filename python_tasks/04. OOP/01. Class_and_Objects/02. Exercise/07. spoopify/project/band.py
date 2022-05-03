from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if any([x for x in self.albums if x.name == album.name]):
            return f'Band {self.name} already has {album.name} in their library.'

        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return f'Album has been published. It cannot be removed.'

                self.albums.remove(album)
                return f'Album {album_name} has been removed.'

        return f'Album {album_name} is not found.'

    def details(self):
        output = f'Band {self.name}'

        for album in self.albums:
            output += '\n'
            output += album.details()

        return output


album = Album("The Sound of Perseverance")
song = Song("Scavenger of Human Sorrow", 6.56, False)
album.add_song(song)
message = album.remove_song("Scavenger of Human Sorrow")
expected = "Removed song Scavenger of Human Sorrow from album The Sound of Perseverance."
