import json


class Albums:
    def __init__(self):
        try:
            with open("albums.json", "r") as f:
                self.albums = json.load(f)
        except FileNotFoundError:
            self.albums = []

    def all(self):
        return self.albums

    def get(self, id):
        return self.albums[id]

    def create(self, data, filename):
        data.pop('csrf_token')
        data['cover'] = filename
        self.albums.append(data)

    def save_all(self):
        with open("albums.json", "w") as f:
            json.dump(self.albums, f)

    def update(self, id, data, filename):
        data.pop('csrf_token')
        data['cover'] = filename
        self.albums[id] = data
        self.save_all()


albums = Albums()
