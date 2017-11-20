from gamemanagerlib.storage.interface import Storage, Record


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

    def read(self, id=None, where=None, contains=None):
        where = where or {}
        contains = contains or {}

        if id:
            record = self.map.get(id)
            return [record] if record else []

        result = list(self.map.values())

        for record in list(result):
            for key, value in contains.items():
                item_value = getattr(record, key)

                if not isinstance(value, list):
                    value = [value]

                if isinstance(item_value, list) and not set(value).issubset(item_value):
                    result.remove(record)

        for record in result:
            matches = True
            for key, value in where.items():
                try:
                    if getattr(record, key) != value:
                        matches = False
                        break
                except AttributeError:
                    continue

            if not matches:
                result.remove(record)

        return result

    def delete(self, id):
        del self.map[id]
