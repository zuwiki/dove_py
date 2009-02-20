class Document(object):
    data = {}
    restricted = ['type']
    def __set__(name, value):
        if name not in self.restricted:
            self.data[name] = value
        else:
            raise RestrictedKeyException(name)

    def __get__(name):
        return self.data[name]

    def json(self):
        js.dumps(self.data)

    def save(self):
        self.provider.save(self.json())
