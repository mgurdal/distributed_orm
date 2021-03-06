import unittest
from mock import patch
from dorm.database import models
from dorm.database import queries
from dorm.database.drivers.base import BaseDriver


class FieldTestCase(unittest.TestCase):
    """Base field object"""

    def setUp(self):
        self.test_field = models.Field('COLUMN_TYPE')

    def test_create_sql(self):
        """Return sql statement for create table."""

        self.test_field.name = 'COLUMN_NAME'

        self.assertEqual("COLUMN_NAME COLUMN_TYPE",
                         self.test_field.create_sql())

    def test__serialize_data(self):
        self.assertEqual(b'test', self.test_field._serialize_data('test'))


class IntegerTestCase(unittest.TestCase):
    """SQLite Integer field"""

    def setUp(self):
        self.test_int_field = models.Integer()

    def test_column_type(self):
        self.assertEqual('INTEGER', self.test_int_field.column_type)

    def test_sql_format(self):
        """sql query format of data"""
        self.assertIsInstance(self.test_int_field.sql_format(20), str)

    def test__serialize_data(self):
        self.assertEqual(self.test_int_field._serialize_data(20), 20)


class FloatTestCase(unittest.TestCase):
    """SQLite Float field"""

    def setUp(self):
        self.test_int_field = models.Float()

    def test_column_type(self):
        self.assertEqual('DOUBLE', self.test_int_field.column_type)

    def test_sql_format(self):
        """sql query format of data"""
        self.assertIsInstance(self.test_int_field.sql_format(20.6), str)

    def test__serialize_data(self):
        self.assertIsInstance(self.test_int_field._serialize_data(20.5), float)
        self.assertEqual(self.test_int_field._serialize_data(20.5), 20.5)


class CharTestCase(unittest.TestCase):
    """SQLite Char field"""

    def setUp(self):
        self.test_char_field = models.Char(max_length=4)

    def test_create_sql(self):
        self.test_char_field.name = 'test'
        self.assertEqual('test CHAR(4)', self.test_char_field.create_sql())

    def test_sql_format(self):
        self.assertEqual("'test'", self.test_char_field.sql_format("test"))

    def test_char_max_length_cannot_be_exceeded(self):
        try:
            self.test_char_field.sql_format("test_ex")
        except Exception as e:
            self.assertEqual('Maximum length exceeded', e.args[0])


class VarcharTestCase(unittest.TestCase):
    """SQLite Varchar field"""

    def setUp(self):
        self.test_char_field = models.Varchar(max_length=4)

    def test_create_sql(self):
        self.test_char_field.name = 'test'
        self.assertEqual('test VARCHAR(4)',
                         self.test_char_field.create_sql())

    def test_sql_format(self):
        self.assertEqual("'test'", self.test_char_field.sql_format("test"))

    def test_char_max_length_cannot_be_exceeded(self):
        try:
            self.test_char_field.sql_format("test_ex")
        except Exception as e:
            self.assertEqual('maximum length exceeded', e.args[0])


class TextTestCase(unittest.TestCase):
    """SQLite Text field"""

    def test_sql_format(self):
        """sql query format of data"""
        self.assertEqual("'test'", models.Text().sql_format('test'))


class DatetimeTestCase(unittest.TestCase):

    def setUp(self):
        self.test_Datetime = models.Datetime()

    def test_sql_format(self):
        """sql query format of data"""
        from datetime import datetime
        self.assertEqual("'2017-07-07 00:00:00'",
                         self.test_Datetime.sql_format(datetime(2017, 7, 7, 0, 0, 0)))

    def test__serialize_data(self):
        from datetime import datetime
        self.assertEqual('2017-07-07 00:00:00',
                         self.test_Datetime._serialize_data(datetime(2017, 7, 7, 0, 0, 0)))


class DateTestCase(unittest.TestCase):
    def setUp(self):
        self.test_date = models.Date()

    def test_sql_format(self):
        """sql query format of data"""
        from datetime import date
        self.assertEqual(
            "'2017-07-07'", self.test_date.sql_format(date(2017, 7, 7)))

    def test__serialize_data(self):
        from datetime import date
        self.assertEqual(
            '2017-07-07', self.test_date._serialize_data(date(2017, 7, 7)))


class TimestampTestCase(unittest.TestCase):

    def setUp(self):
        self.test_timestamp = models.Datetime()

    def test_sql_format(self):
        """sql query format of data"""
        from datetime import datetime
        self.assertEqual("'2017-07-07 00:00:00'",
                         self.test_timestamp.sql_format(datetime(2017, 7, 7, 0, 0, 0)))

    def test__serialize_data(self):
        from datetime import datetime
        self.assertEqual('2017-07-07 00:00:00',
                         self.test_timestamp._serialize_data(datetime(2017, 7, 7, 0, 0, 0)))


class PrimaryKeyTestCase(unittest.TestCase):

    def test_create_sql(self):
        test_pk = models.PrimaryKey()
        test_pk.name = 'test'  # models sets it
        self.assertEqual('test INTEGER NOT NULL PRIMARY KEY',
                         test_pk.create_sql())


class ForeignKeyTestCase(unittest.TestCase):

    def setUp(self):
        self.to_table = models.Model()
        self.to_table.__tablename__ = 'test_table'
        self.to_table.id = 1
        self.test_fk = models.ForeignKey(self.to_table)
        self.test_fk.name = 'test_fk'

    def test_create_sql(self):
        self.assertEqual(
            'test_fk INTEGER NOT NULL REFERENCES test_table (id)', self.test_fk.create_sql())

    def test_sql_format(self):
        """sql query format of data"""
        self.assertEqual("1", self.test_fk.sql_format(self.to_table))

    def test__serialize_data(self):
        """ will be tested after coding is done """
        pass


class ForeignKeyReverseTestCase(unittest.TestCase):

    def test_update_attr(self):
        pass

    def test__query_sql(self):
        pass

    def test_all_method(self):
        pass

    def test_count_method(self):
        pass


class ManyToManyBaseTestCase(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_update_attr(self):
        pass

    def test__query_sql(self):
        pass

    def test_add(self):
        pass

    def test_remove(self):
        pass

    def test_all(self):
        pass

    def test_count(self):
        pass


class ManyToManyTestCase(unittest.TestCase):

    def test_update_attr(self):
        pass

    def test_create_m2m_table(self):
        pass

    def test_drop_m2m_table(self):
        pass

    def test_create_reversed_field(self):
        pass

    def test_delete_reversed_field(self):
        pass


if __name__ == '__main__':
    unittest.main()
