class Song():
    def __init__(self, artists: dict[str] = None, title: str = None, id: str = None, image_url: str = None):
        self.artists = artists
        self.title = title
        self.id = id
        self.image_url = image_url

    def to_dict(self):
        return self.__dict__