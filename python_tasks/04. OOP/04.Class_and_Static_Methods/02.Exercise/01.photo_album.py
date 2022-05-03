from math import ceil


class PhotoAlbum:
    MAX_CAPACITY_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = int(pages)
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / cls.MAX_CAPACITY_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for row in range(len(self.photos)):
            if len(self.photos[row]) >= self.MAX_CAPACITY_PER_PAGE:
                continue
            self.photos[row].append(label)
            photo_place = self.photos[row].index(self.photos[row][-1])  # {len(self.photos[row])} better solution
            return f'{label} photo added successfully on page {row + 1}' \
                   f' slot {photo_place + 1}'

        return 'No more free slots'

    def display(self):
        output = ''
        for row in self.photos:
            output += "-----------\n"  # can make this in separator
            output += " ".join('[]' for _ in row)
            output += '\n'

        return output + "-----------"


album = PhotoAlbum(2)
print('Default:')
print(album.pages)
print(album.photos)
album = PhotoAlbum.from_photos_count(1)
print('New One:')
print(album.pages)
print(album.photos)
