from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__build_photos()

    def __build_photos(self):
        return [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for page_idx in range(len(self.photos)):
            page = self.photos[page_idx]
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {page_idx + 1} slot {len(self.photos[page_idx])}"
        return "No more free slots"

    def display(self):
        separator = "-" * 11
        result = separator + "\n"

        for row in self.photos:
            result += " ".join(["[]" for _ in row]) + "\n"
            result += separator + "\n"

        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())