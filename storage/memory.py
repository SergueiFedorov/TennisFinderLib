from storage.interface import Storage, Record


class MemoryStorage(Storage):

    def __init__(self):
        self.map = {}

    def write(self, record: Record):
        if not record.id:
            record.id = hash(record)
        self.map[record.id] = record
        return record

    def update(self, record: Record):
        return self.write(record)

    def read(self, id=None, where=None):
        where = where or {}

        if id:
            return [self.map[id]]

        result = []
        for _, record in self.map.items():
            matches = True
            for key, value in where.items():
                try:
                    if getattr(record, key) != value:
                        matches = False
                        break
                except AttributeError:
                    continue

            if matches:
                result.append(record)

        return result

    def delete(self, id):
        del self.map[id]
