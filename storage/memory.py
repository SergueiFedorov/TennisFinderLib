import storage.interface


class MemoryStorage(storage.interface.Storage):

    def __init__(self):
        self.map = {}

    def write(self, record : storage.interface.Record):
        if not record.id:
            record.id = hash(record)
        self.map[record.id] = record
        return record

    def read(self, id=None, where=None):
        return self.map[id]

    def delete(self, id):
        del self.map[id]
