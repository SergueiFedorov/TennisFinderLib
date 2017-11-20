import unittest

from gamemanagerlib.storage.memory import MemoryStorage, Record


class Dummy(Record):
    def __init__(self, foo, *args, **kwargs):
        super(Dummy, self).__init__(*args, **kwargs)
        self.foo = foo


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

        self.assertEqual(created_record.id, read_record[0].id)

    def test_get_where(self):

        storage = MemoryStorage()
        storage.map["bar"] = Dummy(foo="bar")
        storage.map["ipsum"] = Dummy(foo="ipsum")

        found = storage.read(where={"foo": "bar"})

        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], storage.map["bar"])

    def test_record_not_found(self):

        storage = MemoryStorage()  # Empty
        result = storage.read(id="foo")

        self.assertEqual(result, [])

    def test_get_in(self):

        storage = MemoryStorage()
        storage.map["bar"] = Dummy(foo=[1, 2])
        storage.map["ipsum"] = Dummy(foo=[4])

        found = storage.read(contains={"foo": [1]})

        self.assertEqual(found[0], storage.map["bar"])

    def test_get_in_not_found(self):

        storage = MemoryStorage()
        storage.map["bar"] = Dummy(foo=[1, 2])
        storage.map["ipsum"] = Dummy(foo=[])

        found = storage.read(contains={"foo": [3]})

        self.assertEqual(len(found), 0)

    def test_get_in_none_array(self):

        storage = MemoryStorage()
        storage.map["bar"] = Dummy(foo=[1, 2])
        storage.map["ipsum"] = Dummy(foo=[4])

        found = storage.read(contains={"foo": 1})

        self.assertEqual(found[0], storage.map["bar"])