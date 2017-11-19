from abc import ABCMeta


class Record(object):

    def __init__(self, id=None):
        self.id = id


class Storage(metaclass=ABCMeta):

    def read(self, id=None, where=None):
        pass

    def write(self, record : Record) -> Record:
        pass

    def delete(self, id):
        pass

    def update(self, record: Record) -> Record:
        pass