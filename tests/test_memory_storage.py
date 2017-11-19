import unittest

from storage.memory import MemoryStorage, Record, Storage


class Tests(unittest.TestCase):

    def test_create_record(self):

        storage = MemoryStorage()

        record = storage.write(Record())

        self.assertIsNotNone(record)
        self.assertIsNotNone(record.id)

    def test_get_record(self):

        storage = MemoryStorage()

        created_record = storage.write(Record())
        read_record = storage.read(created_record.id)

        self.assertEqual(created_record.id, read_record.id)

    def test_get_where(self):

        class Dummy(Record):

            def __init__(self, foo, *args, **kwargs):
                super(Dummy, self).__init__(*args, **kwargs)
                self.foo = foo

        storage = MemoryStorage()
        storage.map["bar"] = Dummy(foo="bar")
        storage.map["ipsum"] = Dummy(foo="ipsum")

        found = storage.read(where={"foo": "bar"})

        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], storage.map["bar"])